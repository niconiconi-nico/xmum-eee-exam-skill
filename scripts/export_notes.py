#!/usr/bin/env python3
"""
Export note-organizer Markdown to A4 PDF.

The script tries, in order:
1. Node Playwright Chromium HTML-to-PDF with page numbers.
2. Python Playwright Chromium HTML-to-PDF with page numbers.
3. Local Chrome/Edge headless HTML-to-PDF.
4. pandoc PDF export.
5. WeasyPrint PDF export.

If PDF export fails, it writes an HTML file and optionally tries docx fallback.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


DEFAULT_CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
body {
  font-family: "Noto Sans CJK SC", "Microsoft YaHei", "PingFang SC", Arial, sans-serif;
  color: #111827;
  line-height: 1.58;
  font-size: 10.5pt;
}
h1, h2, h3, h4 { color: #0f172a; line-height: 1.25; page-break-after: avoid; }
h1 { font-size: 22pt; border-bottom: 2px solid #2563eb; padding-bottom: 6px; }
h2 { font-size: 16pt; margin-top: 22px; }
h3 { font-size: 13pt; margin-top: 16px; }
p, li { overflow-wrap: anywhere; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 9.5pt; }
th, td { border: 1px solid #cbd5e1; padding: 6px 8px; vertical-align: top; }
th { background: #eff6ff; color: #0f172a; }
code { font-family: "Cascadia Mono", Consolas, monospace; background: #f1f5f9; padding: 1px 4px; border-radius: 3px; }
pre { background: #f8fafc; border: 1px solid #cbd5e1; padding: 10px; white-space: pre-wrap; }
blockquote, .callout { border-left: 4px solid #2563eb; background: #eff6ff; color: #0f172a; padding: 9px 12px; margin: 12px 0; }
.warning { border-left-color: #f59e0b; background: #fffbeb; }
.uncertain { border-left-color: #64748b; background: #f8fafc; }
"""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def normalize_callouts(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^>\s*\[!(NOTE|WARNING)\]\s*(.*)$", line)
        if not m:
            out.append(line)
            i += 1
            continue

        kind = m.group(1)
        title = (m.group(2) or ("补充" if kind == "NOTE" else "注意")).strip()
        body_lines: list[str] = []
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            body_lines.append(re.sub(r"^>\s?", "", lines[i]))
            i += 1

        klass = "warning" if kind == "WARNING" else "callout"
        out.append(f'<div class="{klass}"><strong>{html.escape(title)}</strong>')
        if body_lines:
            out.extend(body_lines)
        out.append("</div>")
    return "\n".join(out)


def markdown_to_html(markdown_text: str, title: str, css: str) -> str:
    markdown_text = normalize_callouts(markdown_text)
    try:
        import markdown  # type: ignore

        body = markdown.markdown(
            markdown_text,
            extensions=["extra", "tables", "fenced_code", "sane_lists", "nl2br"],
            output_format="html5",
        )
    except Exception:
        body = simple_markdown(markdown_text)

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>{css}</style>
<script>
window.MathJax = {{
  tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']] }},
  svg: {{ fontCache: 'global' }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>
{body}
</body>
</html>
"""


def find_chromium_executable() -> str | None:
    env_path = os.environ.get("NOTE_ORGANIZER_CHROME")
    if env_path and Path(env_path).exists():
        return env_path

    candidates: list[Path] = []
    if sys.platform.startswith("win"):
        program_files = [os.environ.get("ProgramFiles"), os.environ.get("ProgramFiles(x86)")]
        for root in program_files:
            if root:
                candidates.extend(
                    [
                        Path(root) / "Google/Chrome/Application/chrome.exe",
                        Path(root) / "Microsoft/Edge/Application/msedge.exe",
                    ]
                )
    elif sys.platform == "darwin":
        candidates.extend(
            [
                Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
                Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
            ]
        )
    else:
        for name in ("google-chrome", "chromium", "chromium-browser", "microsoft-edge"):
            found = shutil.which(name)
            if found:
                return found

    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None


def simple_markdown(markdown_text: str) -> str:
    blocks: list[str] = []
    in_ul = False
    in_code = False
    code_lines: list[str] = []

    def close_ul() -> None:
        nonlocal in_ul
        if in_ul:
            blocks.append("</ul>")
            in_ul = False

    for raw in markdown_text.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            if in_code:
                blocks.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                in_code = False
            else:
                close_ul()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            close_ul()
            continue
        heading = re.match(r"^(#{1,4})\s+(.*)$", line)
        if heading:
            close_ul()
            level = len(heading.group(1))
            blocks.append(f"<h{level}>{html.escape(heading.group(2))}</h{level}>")
            continue
        bullet = re.match(r"^\s*[-*]\s+(.*)$", line)
        if bullet:
            if not in_ul:
                blocks.append("<ul>")
                in_ul = True
            blocks.append(f"<li>{html.escape(bullet.group(1))}</li>")
            continue
        close_ul()
        blocks.append(f"<p>{html.escape(line)}</p>")
    close_ul()
    if in_code:
        blocks.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    return "\n".join(blocks)


def node_candidates() -> list[str]:
    candidates: list[str] = []
    found = shutil.which("node")
    if found:
        candidates.append(found)
    bundled = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe"
    if bundled.exists():
        candidates.append(str(bundled))
    bundled_unix = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node"
    if bundled_unix.exists():
        candidates.append(str(bundled_unix))
    return list(dict.fromkeys(candidates))


def node_module_paths() -> list[str]:
    paths: list[str] = []
    existing = os.environ.get("NODE_PATH")
    if existing:
        paths.extend(existing.split(os.pathsep))
    bundled = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules"
    if bundled.exists():
        paths.append(str(bundled))
    return list(dict.fromkeys(paths))


def export_with_node_playwright(html_path: Path, pdf_path: Path) -> None:
    js = r"""
const { chromium } = require('playwright');

(async () => {
  const launchOptions = {};
  if (process.env.CHROME_EXECUTABLE) {
    launchOptions.executablePath = process.env.CHROME_EXECUTABLE;
  }
  const browser = await chromium.launch(launchOptions);
  const page = await browser.newPage();
  await page.goto(process.env.HTML_URL, { waitUntil: 'networkidle' });
  try {
    await page.evaluate(async () => {
      if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
        await MathJax.startup.promise;
      }
    });
  } catch (error) {}
  await page.pdf({
    path: process.env.PDF_PATH,
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: "<div style='font-size:9px;color:#64748b;width:100%;text-align:center;margin:0 auto;'><span class='pageNumber'></span> / <span class='totalPages'></span></div>",
    margin: { top: '18mm', right: '16mm', bottom: '20mm', left: '16mm' }
  });
  await browser.close();
})().catch((error) => {
  console.error(error && error.stack ? error.stack : error);
  process.exit(1);
});
"""
    nodes = node_candidates()
    if not nodes:
        raise RuntimeError("node not found")

    with tempfile.TemporaryDirectory() as tmp:
        js_path = Path(tmp) / "export_pdf.js"
        write_text(js_path, js)
        env = os.environ.copy()
        paths = node_module_paths()
        if paths:
            env["NODE_PATH"] = os.pathsep.join(paths)
        chrome = find_chromium_executable()
        if chrome:
            env["CHROME_EXECUTABLE"] = chrome
        env["HTML_URL"] = html_path.resolve().as_uri()
        env["PDF_PATH"] = str(pdf_path)
        last_error = None
        for node in nodes:
            result = subprocess.run([node, str(js_path)], env=env, text=True, capture_output=True)
            if result.returncode == 0:
                return
            last_error = (result.stderr or result.stdout).strip()
        raise RuntimeError(last_error or "Node Playwright export failed")


def export_with_playwright(html_path: Path, pdf_path: Path) -> None:
    from playwright.sync_api import sync_playwright  # type: ignore

    with sync_playwright() as p:
        chrome = find_chromium_executable()
        browser = p.chromium.launch(executable_path=chrome) if chrome else p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        try:
            page.wait_for_function("window.MathJax && MathJax.startup && MathJax.startup.promise", timeout=5000)
            page.evaluate("MathJax.startup.promise")
        except Exception:
            pass
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=(
                "<div style='font-size:9px;color:#64748b;width:100%;"
                "text-align:center;margin:0 auto;'>"
                "<span class='pageNumber'></span> / <span class='totalPages'></span>"
                "</div>"
            ),
            margin={"top": "18mm", "right": "16mm", "bottom": "20mm", "left": "16mm"},
        )
        browser.close()


def export_with_chrome_cli(html_path: Path, pdf_path: Path) -> None:
    chrome = find_chromium_executable()
    if not chrome:
        raise RuntimeError("Chrome/Edge executable not found")
    with tempfile.TemporaryDirectory() as user_data_dir:
        subprocess.run(
            [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                f"--user-data-dir={user_data_dir}",
                f"--print-to-pdf={pdf_path}",
                html_path.resolve().as_uri(),
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )


def export_with_pandoc(md_path: Path, pdf_path: Path, css_path: Path | None) -> None:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("pandoc not found")
    cmd = [pandoc, str(md_path), "-o", str(pdf_path), "--pdf-engine=xelatex", "-V", "geometry:a4paper,margin=18mm"]
    if css_path:
        cmd.extend(["--css", str(css_path)])
    subprocess.run(cmd, check=True)


def export_with_weasyprint(html_path: Path, pdf_path: Path) -> None:
    from weasyprint import HTML  # type: ignore

    HTML(filename=str(html_path)).write_pdf(str(pdf_path))


def export_docx_with_pandoc(md_path: Path, docx_path: Path) -> bool:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        return False
    subprocess.run([pandoc, str(md_path), "-o", str(docx_path)], check=True)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Export note-organizer Markdown to A4 PDF.")
    parser.add_argument("markdown", type=Path, help="Input Markdown file")
    parser.add_argument("-o", "--output", type=Path, help="Output PDF path")
    parser.add_argument("--title", default=None, help="HTML/PDF document title")
    parser.add_argument("--css", type=Path, default=None, help="Optional CSS file")
    parser.add_argument("--docx-fallback", action="store_true", help="Try docx export if PDF export fails")
    parser.add_argument("--keep-html", action="store_true", help="Keep generated HTML next to the PDF")
    args = parser.parse_args()

    md_path = args.markdown.resolve()
    if not md_path.exists():
        print(f"Input file not found: {md_path}", file=sys.stderr)
        return 2

    pdf_path = (args.output or md_path.with_suffix(".pdf")).resolve()
    html_path = pdf_path.with_suffix(".html")
    docx_path = pdf_path.with_suffix(".docx")
    title = args.title or md_path.stem
    css = read_text(args.css.resolve()) if args.css else DEFAULT_CSS
    css_path = args.css.resolve() if args.css else None

    html_doc = markdown_to_html(read_text(md_path), title, css)
    write_text(html_path, html_doc)

    errors: list[str] = []
    for label, exporter in (
        ("Node Playwright", lambda: export_with_node_playwright(html_path, pdf_path)),
        ("Python Playwright", lambda: export_with_playwright(html_path, pdf_path)),
        ("Chrome/Edge CLI", lambda: export_with_chrome_cli(html_path, pdf_path)),
        ("pandoc", lambda: export_with_pandoc(md_path, pdf_path, css_path)),
        ("WeasyPrint", lambda: export_with_weasyprint(html_path, pdf_path)),
    ):
        try:
            exporter()
            if pdf_path.exists() and pdf_path.stat().st_size > 0:
                if not args.keep_html:
                    try:
                        html_path.unlink()
                    except OSError:
                        pass
                print(f"PDF exported: {pdf_path}")
                return 0
        except Exception as exc:
            errors.append(f"{label}: {exc}")

    print("PDF export failed.", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    print(f"Generated HTML fallback: {html_path}", file=sys.stderr)

    if args.docx_fallback:
        try:
            if export_docx_with_pandoc(md_path, docx_path):
                print(f"DOCX fallback exported: {docx_path}", file=sys.stderr)
            else:
                print("DOCX fallback skipped: pandoc not found.", file=sys.stderr)
        except Exception as exc:
            print(f"DOCX fallback failed: {exc}", file=sys.stderr)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
