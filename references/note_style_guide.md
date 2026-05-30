# Note Style Guide

## Core style

- Write in Chinese first.
- Preserve English technical terms and symbols.
- Use concise English only for important definitions, formula meanings, and canonical terminology.
- Make the result useful for revision, not merely a summary.
- Prefer structured tables for terms, formulas, comparison of methods, and common mistakes.
- Prefer step-by-step bullets for derivations, procedures, and debugging flows.

## Bilingual pattern

For important concepts:

```markdown
### Convolution / 卷积

中文：卷积描述输入信号和系统冲激响应共同决定输出的过程。

English: Convolution describes how the input signal and the impulse response combine to produce the output.
```

For formulas:

```markdown
$$y(t)=x(t)*h(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)d\tau$$

- 中文：输出 $y(t)$ 等于输入 $x(t)$ 与冲激响应 $h(t)$ 的卷积。
- English: The output $y(t)$ is the convolution of the input $x(t)$ and the impulse response $h(t)$.
- When to use / 什么时候用：LTI 系统已知输入和冲激响应时。
```

## Supplement callouts

Use a blue supplement callout for helper explanations, intuition, simple diagrams, or added study tips that are not directly in the lecture material.

```markdown
> [!NOTE] 补充
> 讲义中没有，作为辅助理解：这里可以把系统看成一个 frequency-selective filter。
```

If adding a helper diagram, label it:

```markdown
> [!NOTE] 补充
> 讲义中没有，作为辅助理解：下图是简化示意，不代表老师原图。
```

## Teacher typo callouts

Use this format only when the source appears clearly wrong:

```markdown
> [!WARNING] 老师笔误
> PPT slide 12 写作 `$e^{-st}$`，但根据 Laplace transform definition 应为 `$e^{-st}x(t)$` 出现在积分中。
```

## Uncertainty labels

- `AI推测`: Use when the material is unclear but context supports a likely interpretation.
- `缺少材料`: Use when a page, slide, image, answer, or prerequisite is missing.
- `不确定`: Use when there is a conflict or no reliable way to infer the answer.

Keep uncertainty next to the exact affected content.

## PDF style

Default PDF requirements:

- A4 page size.
- No table of contents unless requested.
- Page numbers in the footer.
- Clear headings and readable tables.
- Blue supplement callouts.
- Mathematical formulas preserved in LaTeX form or rendered clearly when the export tool supports math rendering.
- Avoid very wide tables. Split them into smaller tables if needed.

## What good output feels like

Good output should let the student revise without reopening every lecture file. It should answer:

- What is this chapter about?
- What are the exact definitions and formulas?
- When do I use each formula or method?
- What mistakes are common?
- How would this appear in an exam or tutorial?
- Which parts came from material, which parts are supplement, and which parts are uncertain?
