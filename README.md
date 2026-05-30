# niconiconi XMUM EEE Exam Revision Skill

`note-organizer` 是 niconiconi 考试复习自用 Codex/ChatGPT skill，适用于 XMUM EEE 课程。它用于把大学 EEE、数学、概率、信号与系统、电子器件、嵌入式和 FPGA 等课程材料整理成结构化中英双语复习笔记。

It is designed for organizing lecture PDFs, PPT slides, Word documents, screenshots, formulas, worked examples, teacher solutions, lab notes, embedded-system materials, and FPGA project notes into structured Chinese-English bilingual revision notes.

## ✨ 功能特点

- 支持 PDF、PPT、Word、截图、题目、老师答案和实验材料整理。
- 默认生成中文为主、保留英文术语的中英双语复习笔记。
- 支持一章一章、一讲一讲、一题一题整理。
- 适合 XMUM EEE 相关课程，例如数学、概率、信号与系统、电子器件、嵌入式、FPGA。
- 自动整理核心概念、公式总结、例题讲解、易错点和考试重点。
- 对不确定内容、缺失材料和 AI 补充内容进行明确标注。

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/niconiconi-nico/xmum-eee-exam-skill.git
cd xmum-eee-exam-skill
```

如果你已经在 GitHub 页面下载了 ZIP，也可以直接解压后进入该文件夹。

### 2. 安装到 Codex/ChatGPT skills 目录

把 skill 文件夹复制到你的 Codex/ChatGPT skills 目录中。

推荐结构如下：

```text
<your-skills-directory>/
└── note-organizer/
    ├── SKILL.md
    ├── README.md
    ├── references/
    ├── assets/
    └── scripts/
```

Windows PowerShell 示例：

```powershell
$skills = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force -Path $skills
Copy-Item -Recurse -Force . "$skills\note-organizer"
```

macOS / Linux 示例：

```bash
mkdir -p ~/.codex/skills
cp -r . ~/.codex/skills/note-organizer
```

> 如果你的 Codex/ChatGPT skills 目录不是以上位置，请根据自己的实际环境调整路径。

### 3. 重新加载 skill

安装完成后，重新打开 Codex/ChatGPT，或者新建一个会话，让系统重新扫描 skills。

### 4. 使用示例

```text
用 note-organizer 整理这份 PDF，生成中英双语考试复习笔记。
```

```text
用 note-organizer 按 lecture 一章一章整理这些讲义。
```

```text
用 note-organizer 整理这套题，输出题目翻译、解题步骤、最终答案和易错点。
```

```text
Use note-organizer to turn these lecture slides into structured bilingual revision notes.
```

## 📚 默认输出结构

默认生成的笔记结构如下：

```text
# Chapter / Lecture Title

## 1. Overview / 本章概览
## 2. Key Concepts / 核心概念
## 3. Formula Summary / 公式总结
## 4. Detailed Explanation / 详细讲解
## 5. Worked Examples / 例题
## 6. Exam Focus / 考点
## 7. Summary Checklist / 复习清单
```

对于题目类材料，默认使用：

```text
## Question / 题目
## Translation / 中文翻译
## Given / 已知条件
## Method / 解题思路
## Solution / 详细解答
## Final Answer / 最终答案
## Common Mistake / 易错点
```

## 🧠 适用课程

这个 skill 主要适用于 XMUM EEE 相关课程，包括但不限于：

- Engineering Mathematics
- Probability and Statistics
- Signals and Systems
- Electronic Devices
- Circuit Analysis
- Embedded Systems
- FPGA / Digital Design
- Microcontroller projects
- Engineering lab reports and project notes

## 📄 输出格式

默认输出 Markdown 笔记。

如果用户明确要求，可以进一步整理为：

- Word / `.docx`
- PDF
- Cheat sheet / 公式表
- Exam revision notes / 考试复习笔记
- Worked example collection / 例题集

PDF 或 Word 导出属于可选功能，不作为默认行为。

## ⚠️ 注意事项

- 不要把老师原文大段照抄成笔记。
- 不确定的地方必须标注“不确定”。
- 如果材料不完整，必须说明缺少哪些内容。
- AI 自己补充的解释必须标注为“AI 补充”。
- 如果题目或公式看不清楚，不能乱猜，要提醒用户重新上传清晰版本。
- 默认以考试复习为目标，而不是简单摘要。

## 📁 文件结构

```text
note-organizer/
├── SKILL.md
├── README.md
├── references/
│   ├── note_style_guide.md
│   ├── subject_rules.md
│   ├── output_templates.md
│   └── examples.md
├── assets/
└── scripts/
```

## 📝 License

This is a personal study skill for niconiconi's XMUM EEE exam revision.
Do not redistribute course materials, lecture notes, teacher solutions, or copyrighted documents without permission.
