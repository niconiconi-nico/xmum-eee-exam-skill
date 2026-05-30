# niconiconi考试复习自用skill

`note-organizer` 是 niconiconi 考试复习自用 Codex/ChatGPT skill，用来把大学 EEE、数学、概率、信号与系统、电子器件、嵌入式和 FPGA 等课程材料整理成结构化中英双语复习笔记。

## What it does

- Organizes PDF, PPT, Word, screenshots, handwritten notes, teacher answers, problem sets, transcripts, code, and lab materials.
- Defaults to chapter-by-chapter or lecture-by-lecture notes.
- Separates revision notes and worked solutions unless explicitly asked to merge them.
- Writes mainly in Chinese while preserving English technical terms.
- Adds bilingual explanations for important definitions and formulas.
- Exports A4 PDF by default through `scripts/export_notes.py`.

## Install for Codex

Place this folder at:

```text
C:\Users\27979\.codex\skills\note-organizer
```

Then start a new Codex thread or reload skills. Use:

```text
用 note-organizer 整理这份 PDF
```

## Export Markdown to PDF

From the skill folder:

```powershell
python .\scripts\export_notes.py .\my_notes.md -o .\my_notes.pdf --docx-fallback
```

The script tries Playwright, pandoc, and WeasyPrint. If PDF export fails, it keeps an HTML fallback and can try docx fallback with pandoc.

## Default output

- A4 PDF.
- No table of contents by default.
- Page numbers in the footer.
- Chinese-first explanations.
- Important definitions and formulas bilingual.
- Blue `补充` callout boxes.
