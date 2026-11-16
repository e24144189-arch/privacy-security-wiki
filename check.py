#!/usr/bin/env python3
"""check.py - 簡報檢查腳本（只讀取、只出報告，不會修改任何簡報或 wiki 檔案）

用法（在專案根目錄執行）：
    python check.py                          # 檢查 output/deck.html
    python check.py --round 2                # 報告存成 output/check-report-round2.md
    python check.py --deck output/deck.html --round 1

結束代碼：0 = 全部通過，1 = 有未通過項目（供 SKILL.md 的 loop 判斷）。
只用 Python 標準函式庫；文字溢出檢查需要 playwright，沒裝會顯示 SKIP（不算失敗）。
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

MIN_SLIDES, MAX_SLIDES = 8, 15
MAX_CHARS_WARN = 400  # 單頁字數超過只警告，不算失敗

# 專案已確認不得出現在簡報的字眼（來自 lint 與 AGENTS.md 規則）
FORBIDDEN = ["脫離歐盟", "特種個資", "特種個", "改列第三章之一",
             "移交個資會", "不強制定期", "安全提問"]


def strip_tags(html):
    html = re.sub(r"<(script|style)\b.*?</\1>", "", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", text).strip()


def get_slides(html):
    """回傳 [(slide_no, body_html, attrs)]，slide 為 class 含 slide 的 <section>。"""
    slides = []
    for attrs, body in re.findall(r"<section\b([^>]*)>(.*?)</section>", html, flags=re.S | re.I):
        m = re.search(r'class\s*=\s*["\']([^"\']*)["\']', attrs, flags=re.I)
        if m and re.search(r"\bslide\b", m.group(1)):
            slides.append((len(slides) + 1, body, attrs))
    return slides


def get_sources(body):
    """取出 class 含 source 的元素內所有 wiki/raw 路徑。"""
    paths = []
    for _, inner in re.findall(
            r'<(\w+)\b[^>]*class\s*=\s*["\'][^"\']*\bsource\b[^"\']*["\'][^>]*>(.*?)</\1>',
            body, flags=re.S | re.I):
        paths += re.findall(r"(?:wiki|raw)/[\w\-./]+\.md", strip_tags(inner))
    return paths


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--deck", default="output/deck.html")
    ap.add_argument("--round", type=int, default=1)
    args = ap.parse_args()

    root = Path.cwd()
    deck = root / args.deck
    if not deck.exists():
        print(f"找不到簡報檔：{deck}")
        sys.exit(1)
    html = deck.read_text(encoding="utf-8")
    # 先移除 <style>、<script>、HTML 註解，避免其中的字樣被誤當成投影片或內容
    html_clean = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    html_clean = re.sub(r"<(style|script)\b.*?</\1>", "", html_clean, flags=re.S | re.I)
    slides = get_slides(html_clean)

    results = []  # (編號, 項目, 狀態PASS/FAIL/WARN/SKIP, [細節])
    no_slides = len(slides) == 0
    NOSLIDE_MSG = ["找不到任何 <section class=\"slide\">，此項無法檢查（不算通過）"]

    # 1. 頁數
    n = len(slides)
    ok = MIN_SLIDES <= n <= MAX_SLIDES
    detail = [f"目前共 {n} 頁"]
    if n == 0:
        detail.append("簡報格式不符 SKILL.md 第 3 節：每張投影片必須是 <section class=\"slide\">")
    results.append(("1", f"頁數 {MIN_SLIDES}–{MAX_SLIDES}", "PASS" if ok else "FAIL", detail))

    # 2. 每頁有出處（可用 data-no-source="true" 豁免封面與結尾，最多 2 頁）
    missing, exempt = [], 0
    for no, body, attrs in slides:
        if re.search(r'data-no-source\s*=\s*["\']true["\']', attrs, flags=re.I):
            exempt += 1
            continue
        if not get_sources(body):
            missing.append(f"第 {no} 頁沒有 class=\"source\" 的出處（需列出 wiki/....md 路徑）")
    if exempt > 2:
        missing.append(f"豁免頁 {exempt} 頁，超過上限 2 頁")
    if no_slides:
        results.append(("2", "每頁都有出處", "SKIP", NOSLIDE_MSG))
    else:
        results.append(("2", "每頁都有出處", "FAIL" if missing else "PASS", missing or [f"豁免 {exempt} 頁"]))

    # 3. 引用的頁面存在，且只引用 wiki/（不得直接引用 raw/）
    problems = []
    for no, body, _ in slides:
        for p in get_sources(body):
            if p.startswith("raw/"):
                problems.append(f"第 {no} 頁引用 {p}：簡報只能使用 wiki/，不得引用 raw/")
            elif not (root / p).exists():
                problems.append(f"第 {no} 頁引用的 {p} 不存在")
    if no_slides:
        results.append(("3", "引用的 wiki 頁面存在且不引用 raw/", "SKIP", NOSLIDE_MSG))
    else:
        results.append(("3", "引用的 wiki 頁面存在且不引用 raw/", "FAIL" if problems else "PASS",
                        problems or ["所有引用路徑皆存在"]))

    # 4. 禁用字眼
    text_all = strip_tags(html_clean)
    hits = []
    for no, body, _ in slides:
        t = strip_tags(body)
        for w in FORBIDDEN:
            if w in t:
                hits.append(f"第 {no} 頁出現「{w}」")
    if no_slides:  # 沒有投影片結構時，改掃整份文件
        hits += [f"整份文件出現「{w}」" for w in FORBIDDEN if w in text_all]
    results.append(("4", "不含已確認禁用字眼", "FAIL" if hits else "PASS", hits or ["未發現"]))

    # 5. 72 小時歸屬：含「72」的頁面必須註明是數發部或 GDPR；與個資法並列時警告
    bad72, warn72 = [], []
    for no, body, _ in slides:
        t = strip_tags(body)
        if re.search(r"72", t):
            if not re.search(r"數發部|GDPR", t, flags=re.I):
                bad72.append(f"第 {no} 頁提到 72 但未註明來源是數發部呼籲或 GDPR")
            if "個資法" in t and not re.search(r"未載|未規定|沒有規定|非個資法|不是", t):
                warn72.append(f"第 {no} 頁同時出現「個資法」與 72，請人工確認沒有把 72 小時歸給個資法")
    st = "FAIL" if bad72 else ("WARN" if warn72 else "PASS")
    if no_slides:
        results.append(("5", "72 小時歸屬", "SKIP", NOSLIDE_MSG))
    else:
        results.append(("5", "72 小時歸屬", st, bad72 + warn72 or ["未發現問題"]))

    # 6. 自包含：不得載入外部資源
    ext = re.findall(r"<(?:script|link|img|iframe|source)\b[^>]*(?:src|href)\s*=\s*[\"']\s*(?:https?:)?//[^\"']*",
                     html_clean, flags=re.I)
    ext += re.findall(r"url\(\s*[\"']?https?://[^)]*\)|@import\s+[\"']?https?://[^;]*", html, flags=re.I)
    results.append(("6", "單一自包含 HTML（無外部資源）", "FAIL" if ext else "PASS",
                    [e[:80] for e in ext] or ["未發現外部資源"]))

    # 7. 單頁字數（只警告）
    long_pages = []
    for no, body, _ in slides:
        c = len(strip_tags(body))
        if c > MAX_CHARS_WARN:
            long_pages.append(f"第 {no} 頁約 {c} 字，超過 {MAX_CHARS_WARN} 字，教學簡報建議精簡")
    if no_slides:
        results.append(("7", "單頁字數（警告，不算失敗）", "SKIP", NOSLIDE_MSG))
    else:
        results.append(("7", "單頁字數（警告，不算失敗）", "WARN" if long_pages else "PASS",
                        long_pages or ["皆在範圍內"]))

    # 8. 文字溢出（需要 playwright；沒有就 SKIP）
    #    逐頁用鍵盤右鍵切換，量「目前可見」那一頁：內容是否超出版面，或蓋到底部出處列
    try:
        from playwright.sync_api import sync_playwright
        JS = """() => {
            const all = [...document.querySelectorAll('section.slide')];
            const out = [];
            all.forEach((e, i) => {
                if (e.offsetHeight === 0) return;           // 隱藏的頁不量
                let over = e.scrollHeight > e.clientHeight + 2 || e.scrollWidth > e.clientWidth + 2;
                let overlap = false;
                const src = e.querySelector('.source');
                if (src) {
                    const top = src.getBoundingClientRect().top;
                    e.querySelectorAll('*').forEach(c => {
                        if (c === src || src.contains(c)) return;
                        const r = c.getBoundingClientRect();
                        if (r.height > 0 && r.bottom > top + 2) overlap = true;
                    });
                }
                out.push({i: i + 1, over, overlap});
            });
            return out;
        }"""
        seen, bad = {}, []
        with sync_playwright() as pw:
            br = pw.chromium.launch()
            pg = br.new_page(viewport={"width": 1280, "height": 720}, reduced_motion="reduce")  # 關閉動畫，避免量到動畫中途
            pg.goto(deck.resolve().as_uri())
            for _ in range(n + 2):
                for r in pg.evaluate(JS):
                    seen[r["i"]] = r
                pg.keyboard.press("ArrowRight")
                pg.wait_for_timeout(60)
            br.close()
        for i in sorted(seen):
            r = seen[i]
            if r["over"]:
                bad.append(f"第 {i} 頁內容超出版面（1280×720）")
            if r["overlap"]:
                bad.append(f"第 {i} 頁內容蓋到底部出處列")
        if len(seen) < n:
            bad.append(f"只量到 {len(seen)}/{n} 頁（換頁方式不是鍵盤右鍵？請人工逐頁檢查）")
        results.append(("8", "文字未溢出版面", "FAIL" if bad else "PASS", bad or [f"已逐頁量測 {len(seen)} 頁，皆未溢出"]))
    except Exception as e:  # playwright 未安裝或瀏覽器無法啟動
        results.append(("8", "文字未溢出版面", "SKIP", [f"略過（{type(e).__name__}）：未安裝 playwright，請改用人工逐頁檢查"]))

    # 輸出
    failed = [r for r in results if r[2] == "FAIL"]
    out_dir = root / "output"
    out_dir.mkdir(exist_ok=True)
    report = out_dir / f"check-report-round{args.round}.md"
    lines = [f"# 簡報檢查報告 第 {args.round} 輪",
             f"- 檢查時間：{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
             f"- 檔案：{args.deck}",
             f"- 結果：{'通過' if not failed else f'未通過（{len(failed)} 項 FAIL）'}", "",
             "| # | 項目 | 結果 |", "|---|---|---|"]
    lines += [f"| {a} | {b} | {c} |" for a, b, c, _ in results]
    lines.append("")
    for a, b, c, d in results:
        if c in ("FAIL", "WARN", "SKIP"):
            lines.append(f"## {a}. {b}（{c}）")
            lines += [f"- {x}" for x in d]
            lines.append("")
    report.write_text("\n".join(lines), encoding="utf-8")

    for a, b, c, d in results:
        print(f"[{c:4}] {a}. {b}")
        if c != "PASS":
            for x in d:
                print(f"        - {x}")
    print(f"\n報告已存到 {report}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
