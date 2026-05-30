# niconiconi XMUM EEE Exam Revision Skill

`note-organizer` is niconiconi's personal Codex/ChatGPT skill for XMUM EEE exam revision. It helps organize university EEE, mathematics, probability, signals and systems, electronic devices, embedded systems, and FPGA course materials into structured Chinese-English bilingual revision notes.

It is designed for lecture PDFs, PPT slides, Word documents, screenshots, formulas, worked examples, teacher solutions, lab notes, embedded-system materials, and FPGA project notes.

## Features

- Organizes PDFs, PPT slides, Word documents, screenshots, problem sets, teacher solutions, and lab materials.
- Produces revision notes mainly in Chinese while preserving important English technical terms.
- Supports chapter-by-chapter, lecture-by-lecture, and problem-by-problem organization.
- Fits XMUM EEE courses such as mathematics, probability, signals and systems, electronic devices, embedded systems, and FPGA.
- Extracts key concepts, formula summaries, worked examples, common mistakes, and exam focus points.
- Marks uncertain content, missing material, and AI-added explanations clearly.

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/niconiconi-nico/xmum-eee-exam-skill.git
cd xmum-eee-exam-skill
```

If you downloaded the repository as a ZIP file from GitHub, unzip it and open the extracted folder.

### 2. Install into your Codex/ChatGPT skills directory

Copy this skill folder into your Codex/ChatGPT skills directory.

Recommended layout:

```text
<your-skills-directory>/
`-- note-organizer/
    |-- SKILL.md
    |-- README.md
    |-- references/
    |-- assets/
    `-- scripts/
```

Windows PowerShell example:

```powershell
$skills = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force -Path $skills
Copy-Item -Recurse -Force . "$skills\note-organizer"
```

macOS / Linux example:

```bash
mkdir -p ~/.codex/skills
cp -r . ~/.codex/skills/note-organizer
```

If your Codex/ChatGPT skills directory is different, adjust the destination path for your own environment.

### 3. Reload skills

After installation, restart Codex/ChatGPT or open a new conversation so the app can rescan available skills.

### 4. Use the skill

```text
Use note-organizer to organize this PDF into Chinese-English exam revision notes.
```

```text
Use note-organizer to organize these lecture slides lecture by lecture.
```

```text
Use note-organizer to organize this problem set with translations, solution steps, final answers, and common mistakes.
```

```text
Use note-organizer to turn these FPGA lab notes into structured revision notes.
```

## Default Note Structure

For lecture or chapter materials, the default structure is:

```text
# Chapter / Lecture Title

## 1. Overview
## 2. Key Concepts
## 3. Formula Summary
## 4. Detailed Explanation
## 5. Worked Examples
## 6. Exam Focus
## 7. Summary Checklist
```

For problem-based materials, the default structure is:

```text
## Question
## Translation
## Given
## Method
## Solution
## Final Answer
## Common Mistake
## Exam Focus
```

## Supported Courses

This skill is mainly intended for XMUM EEE-related courses, including but not limited to:

- Engineering Mathematics
- Probability and Statistics
- Signals and Systems
- Electronic Devices
- Circuit Analysis
- Embedded Systems
- FPGA / Digital Design
- Microcontroller projects
- Engineering lab reports and project notes

## Output Formats

The default output is structured Markdown notes.

When requested, the notes can also be prepared as:

- Word / `.docx`
- PDF
- Cheat sheet
- Formula sheet
- Exam revision notes
- Worked example collection

PDF and Word export are optional workflows, not the default behavior.

## Notes and Safety

- Do not copy long passages from teacher materials directly into the notes.
- Mark uncertain content clearly.
- If material is incomplete, state what is missing.
- Mark AI-added explanations as "AI supplement".
- If a question, formula, screenshot, or handwritten note is unreadable, ask for a clearer upload instead of guessing.
- Keep the output focused on exam revision, not simple summarization.

## Repository Structure

```text
note-organizer/
|-- SKILL.md
|-- README.md
|-- references/
|   |-- note_style_guide.md
|   |-- subject_rules.md
|   |-- output_templates.md
|   `-- examples.md
|-- assets/
`-- scripts/
```

## Optional Markdown Export

The repository includes a helper script for exporting Markdown notes when the local environment has suitable tools available:

```bash
python scripts/export_notes.py my_notes.md -o my_notes.pdf --docx-fallback
```

This helper is optional. The skill itself can still be used to organize notes without running the script.

## License

This is a personal study skill for niconiconi's XMUM EEE exam revision.
Do not redistribute course materials, lecture notes, teacher solutions, or copyrighted documents without permission.
