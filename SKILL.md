---
name: note-organizer
description: 用于整理课程讲义、PDF、PPT、Word、截图、课堂笔记、题目、老师答案、手写解题过程、视频转录文本和代码/实验材料，生成结构化复习笔记、双语题解、章节总结、公式/考点整理和可导出的 PDF。当用户要求“用 note-organizer 整理”“整理笔记”“一章一章整理”“逐题讲解”“生成复习资料”“根据讲义/PPT/PDF整理内容”“做 formula sheet / cheat sheet”时使用，特别适合大学 EEE、数学、概率、信号与系统、电子器件、嵌入式和 FPGA 课程。
---

# Note Organizer

## When to use this skill

Use this skill when the user wants course materials turned into review-ready notes or problem solutions. Prefer it for:

- Organizing PDF lectures, PPT slides, Word handouts, screenshots, handwritten work, teacher solutions, problem sets, transcripts, code, or lab material.
- Creating chapter-by-chapter or lecture-by-lecture revision notes.
- Creating separate worked-solution notes for exercises, tutorials, past paper questions, or teacher answers.
- Producing bilingual study material where Chinese is primary and English terms are preserved.
- Exporting polished A4 PDF notes from structured Markdown.
- Making formula summaries, exam-focus notes, checklists, or compact cheat sheets from course material.

## When not to use this skill

Do not use this skill when the user asks for unrelated work such as building apps, writing essays, creating images, searching news, or giving a short standalone concept explanation that does not require note organization.

Do not treat this skill as a homework-submission generator. The job is to organize, explain, check, and structure learning material. Do not invent teacher-provided conclusions or present uncertain reasoning as source material.

## Input handling rules

1. Inspect the uploaded materials before deciding the output structure. Identify whether the material is lecture content, problem sets, teacher answers, handwritten work, code/lab material, or a mixture.
2. Prioritize PDF and PPT material when multiple sources conflict, unless the user says another source is authoritative.
3. Preserve the teacher's terminology, notation, definitions, theorem conditions, variable names, and diagram labels when they are clear.
4. If a scanned page, screenshot, or handwriting is unclear, mark the affected statement as `AI推测` or `缺少材料`; do not silently guess.
5. If lecture notes and problems are both present, create two separate outputs by default: `章节复习笔记` and `逐题题解`. Combine them only when the user explicitly asks.
6. If code or lab material is included, explain hardware connections, code logic, data flow, timing, debug steps, and common failure points; do not rewrite the whole project unless requested.
7. If the material contains an obvious typo or contradiction, correct it only when the correction is strongly supported by context. Mark it as `老师笔误`, include the local source such as `PPT slide X` or `PDF p.X`, and explain the reason briefly.

## Output selection rules

Default output:

- Generate structured Markdown first.
- Export the Markdown to an A4 PDF by default.
- Do not include a table of contents unless the user asks.
- Include page numbers in the final PDF.
- Use Chinese as the main explanation language, preserve English technical terms, and write important definitions and formula meanings in both Chinese and English.
- Render `补充` sections as blue callout boxes in PDF/Word when possible.

Fallback:

- If PDF export fails, keep the complete Markdown file, try to export docx, and tell the user why PDF export failed.
- Use `scripts/export_notes.py` when a lightweight Markdown-to-PDF conversion helper is useful.
- Use `assets/optional_templates/note_pdf.css` for A4 styling and blue supplement boxes.

## Default note structure

Use the following structure by default for chapter or lecture notes, adjusting only when the material clearly needs a different shape:

```markdown
# Chapter / Lecture Title

## 1. Overview / 本章概览
- 本章学什么
- 为什么重要
- 和考试/作业的关系

## 2. Key Concepts / 核心概念
| English Term | 中文解释 | Meaning | Common mistake |
| --- | --- | --- | --- |

## 3. Formula Summary / 公式总结
| Formula | Meaning | When to use | Notes |
| --- | --- | --- | --- |

## 4. Detailed Explanation / 详细讲解
按知识点分节解释。公式推导按老师材料的深度展开。英文术语后面加中文解释。

## 5. Worked Examples / 例题
每题使用固定题解结构。

## 6. Exam Focus / 考点
- 老师可能怎么考
- 常见题型
- 快速判断方法

## 7. Summary Checklist / 复习清单
- 我是否理解……
- 我是否会计算……
- 我是否知道什么时候用……
```

For problem solutions, use this fixed structure:

```markdown
## Problem N / 题目 N

- Question / 题目原文
- Translation / 中文翻译
- Given / 已知条件
- Method / 解题思路
- Solution / 详细解答
- Final Answer / 最终答案
- Common Mistake / 易错点
- Exam Focus / 考点
```

## Bilingual explanation rules

1. Write explanations primarily in Chinese.
2. Preserve English technical terms, symbols, and course-specific names, for example `Fourier transform`, `Laplace transform`, `Z-transform`, `convolution`, `MOSFET`, `energy band diagram`, `interrupt`, `timing constraint`.
3. For important definitions, write both:
   - 中文：严格、可复习的解释。
   - English: a concise technical meaning.
4. For important formulas, write both:
   - 中文：公式含义、变量含义、什么时候用。
   - English: meaning and use case.
5. Do not translate notation or standard abbreviations unnaturally. Keep symbols exactly as in the course material unless correcting a marked `老师笔误`.

## Math and engineering formatting rules

1. Write formulas in LaTeX Markdown: inline `$x(t)$`, display `$$X(s)=\mathcal{L}\{x(t)\}$$`.
2. Keep derivation depth aligned with teacher solutions. If the teacher solution skips algebra, do not over-expand unless the user asks for detailed explanation.
3. Define variables before using them when the material does not already do so clearly.
4. For tables, keep columns short enough for PDF. Split very wide tables into multiple tables.
5. For circuits, systems, device structures, and embedded/FPGA flows, describe diagrams textually if the original image cannot be reproduced.
6. You may add a simple helper diagram when it improves understanding. Mark it clearly as `补充：讲义中没有，作为辅助理解`.

## Source/citation/page-reference rules

1. Do not cite every definition or formula by default.
2. Cite the local source only for corrections, uncertainty, suspected teacher typos, unclear material, conflicting material, or user-requested traceability.
3. Use compact source labels such as `PDF p.12`, `PPT slide 8`, `截图 2`, `老师答案`, or `手写笔记`.
4. If correcting a source error, use this form:
   `老师笔误：PPT slide X 写作 "..."; 根据公式/上下文应为 "...".`
5. Final PDF pages must have page numbers even when content-level source citations are not used.

## Uncertainty handling rules

Use explicit labels:

- `AI推测`: The material is incomplete or unclear, but a reasonable inference can be made.
- `缺少材料`: The answer depends on missing pages, missing slides, unreadable screenshots, or unavailable context.
- `不确定`: There is a conflict or insufficient evidence and no reliable inference.

Do not hide uncertainty inside confident prose. Put uncertainty close to the affected formula, statement, step, or answer.

## Copyright and academic integrity rules

1. Summarize, reorganize, and explain. Do not reproduce long passages from lecture notes, textbooks, or teacher answers.
2. Preserve short exact wording only when needed for definitions, theorem statements, formulas, or problem text.
3. Do not fabricate teacher-provided results, exam hints, or course policies.
4. Do not present `AI推测` or `补充` as original lecture content.
5. For teacher answers, organize and clarify the reasoning while keeping the teacher's solution path.

## Subject-specific templates

Read `references/subject_rules.md` when organizing a specific subject. Use these defaults:

- Mathematics and probability: definitions, assumptions, theorem conditions, formula applicability, examples, common mistake patterns.
- Signals and systems: Fourier/Laplace/Z-transform, convolution, impulse response, transfer function, system properties, poles/zeros, stability, causality.
- Electronic devices: energy band diagram, carrier movement, device operation, I-V characteristics, operating regions, applications.
- Embedded systems and FPGA: hardware connections, registers, timing, interrupts, code logic, state machines, constraints, debug steps.

Use `references/output_templates.md` for reusable Markdown templates. Use `references/note_style_guide.md` for tone, bilingual style, callouts, and PDF expectations. Use `references/examples.md` for trigger and non-trigger examples.

## Final checklist before responding

Before giving the final answer or exported files, verify:

- The output is organized by chapter/lecture unless the user requested another structure.
- Notes and problem solutions are separated by default.
- Important terms and formulas are bilingual.
- Formulas are readable and formatted in LaTeX Markdown.
- Teacher-solution derivations follow the teacher's depth and order.
- Unclear content is marked `AI推测`, `缺少材料`, or `不确定`.
- Corrections to material are marked `老师笔误` with source labels.
- Added helper explanations or diagrams are marked `补充`.
- The PDF is A4, has page numbers, has no table of contents by default, and renders supplement boxes in blue when possible.
- If PDF export failed, Markdown is complete and the failure reason is reported.
