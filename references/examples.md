# Examples

## Requests that should trigger this skill

- 用 note-organizer 整理这份 PDF。
- 用 note-organizer 把这个 PPT 一章一章整理成复习笔记。
- 根据这份讲义生成中英双语笔记，并导出 PDF。
- 把这些题目逐题讲解，整理成 PDF。
- 根据老师答案整理题解、易错点和考点。
- 把这章信号与系统内容做成 formula sheet。
- 整理这个 FPGA lab 的硬件连接、代码逻辑和 debug steps。
- 把截图里的老师板书整理成复习笔记。

## Requests that should not trigger this skill

- 帮我写一个网站。
- 帮我生成一张图片。
- 查一下今天的新闻。
- 直接翻译这份文档，不需要整理。
- 帮我写一篇论文。
- 这个公式是什么意思？给我一句话解释。

## Good response behavior

If the user uploads a PDF and says "用 note-organizer 整理":

1. Inspect the PDF.
2. Identify chapters/lectures and whether there are problems.
3. Produce structured Markdown.
4. Export A4 PDF by default.
5. If there are both lecture notes and problems, keep `章节复习笔记` and `逐题题解` separate.

If the user uploads PPT slides and screenshots:

1. Treat PPT as the main source.
2. Use screenshots as supplements or teacher-board context.
3. Mark unclear screenshot content as `AI推测` or `缺少材料`.
4. If a slide has a likely typo, mark `老师笔误` with slide number.

If the user asks for a cheat sheet:

1. Compress content aggressively.
2. Keep definitions, formulas, conditions, and method-selection cues.
3. Avoid long derivations unless required for exam use.

If the user asks for detailed notes:

1. Keep the default chapter structure.
2. Explain concepts thoroughly.
3. Follow teacher solution depth for derivations.
4. Add `补充` callouts for intuition when helpful.
