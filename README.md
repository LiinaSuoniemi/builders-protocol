# Builder's Protocol

A six-tool pipeline for building AI-assisted software safely.

Built for solo developers and first-time builders who use Claude Code. Gives structure to the full build cycle - from rough idea to deployed product - with security checks at every stage.

---

## What problem this solves

When you build with AI assistance, it is easy to end up with code that works but nobody fully understands. Or code that ships before anyone checked whether it is safe. Or a half-finished idea that becomes a half-finished product because the brief was never clear.

Builder's Protocol gives you six focused tools, each with one job, used in order. Together they cover the full journey from "I have an idea" to "this is ready to ship."

---

## The pipeline

```
BRAINSTORM → CODEMAKER → VIBECODER → CODEKEEPER → GUARDIAN → SENTINEL
```

| Step | Tool | What it does |
|------|------|-------------|
| 0 | BRAINSTORM | Turns a rough idea into a clear plan before anything gets built |
| 1 | CODEMAKER | Builds new projects from scratch - clean, safe, documented |
| 2 | VIBECODER | Scans what was built and reports what to watch out for |
| 3 | CODEKEEPER | Maintains, fixes, and extends existing code |
| 4 | GUARDIAN | Reviews everything before it goes live |
| 5 | SENTINEL | Tests AI systems for security vulnerabilities |

Each tool hands off to the next. BRAINSTORM produces a brief CODEMAKER can start from directly. VIBECODER documents what CODEMAKER built so CODEKEEPER can work safely. GUARDIAN reviews before SENTINEL tests.

You do not have to use all six every time. A small fix might only need CODEKEEPER and GUARDIAN. A new project starts at BRAINSTORM. An inherited codebase starts at VIBECODER.

---

## Who this is for

Builders who:
- Use Claude Code to write code, with or without a strong technical background
- Work alone or in a small team
- Want structure and safety checks without needing a full development team
- Are building AI applications that will have real users

---

## What is a Claude Code skill?

**Claude Code** is a tool made by Anthropic that lets you work with Claude directly in your terminal or code editor. It can read your files, write code, run commands, and help you build software.

A **skill** is a set of instructions that gives Claude Code a specific role. When you activate a skill, Claude stops being a general assistant and becomes that specific tool - with focused rules, a defined way of working, and a structured output.

Think of it like this. Claude Code is the engine. Skills are the different modes you can run it in. BRAINSTORM mode asks questions and maps out plans. CODEMAKER mode builds things. SENTINEL mode tests for security problems. Each mode has its own rules and its own job.

Skills live in a folder on your computer. You activate them by typing a slash command in Claude Code, like `/brainstorm` or `/sentinel`.

---

## How to install

**Step 1.** Download or clone this repository.

**Step 2.** Copy the folders inside `skills/` into your Claude Code skills directory.

On Mac or Linux:
```
~/.claude/skills/
```

On Windows:
```
C:\Users\[your-username]\.claude\skills\
```

Each tool is a folder with a `SKILL.md` file inside. The folder name becomes the command you type to activate it.

**Step 3.** Open a Claude Code session and activate any tool by typing its name with a slash:
```
/brainstorm
/codemaker
/vibecoder
/codekeeper
/guardian
/sentinel
```

---

## New to Claude Code?

If you have never used Claude Code before, start with Jon Gerton's community before installing skills.

**You Craft and AI Helps** - [join here (free)](https://www.skool.com/you-craft-ai-helps/about?ref=37798d7ddad04c0eba94008aa147ebed)

Jon teaches Claude Code from the beginning - what it is, how to set it up, how to actually use it. There are 7 courses and 84 modules covering the basics through advanced workflows. Free to join. Once you have the basics down, come back here and the skills will make immediate sense.

---

## Configuration

Some tools have an **ADAPT THIS SECTION** block inside the SKILL.md file. Fill it in with your project details before running the tool. This is where you tell the tool your project name, tech stack, known issues, and any areas that need extra care.

**GUARDIAN** has an alert email field. Replace `[YOUR_ALERT_EMAIL]` with your address to receive a notification when critical security findings are found.

---

## Review reports saved automatically

VIBECODER, CODEKEEPER, GUARDIAN, and SENTINEL save their reports to a file automatically after each run:

```
[your-project-folder]/reviews/TOOLNAME-YYYYMMDD.md
```

Every review is saved as a dated file. You build up a review history for your project over time without any extra steps.

---

## Going further - reminders and project context

The skills work as standalone tools. No extra setup required.

But if you find yourself forgetting which tool to use next, or losing context between sessions, Claude Code has two features worth knowing about.

**Hooks** are small reminders you can set up in Claude Code's settings. They fire automatically at specific moments — at the start of a session, after each response, when a file is written. You can use them to display the pipeline order every time you open Claude Code, or to prompt yourself to run GUARDIAN before pushing code. If you are the kind of person who gets deep into building and forgets the safety steps, hooks solve that.

**Project instructions** let you write a persistent note that Claude Code reads at the start of every session. Your tech stack, your rules, which tool handles which job. You write it once in a file called `CLAUDE.md` in your project folder. Every session starts with that context already loaded - you do not have to re-explain your project each time.

**A personal context file** takes this further. Some builders keep a separate file with their current priorities, energy level, active projects, and working preferences. Claude Code can be set up to read this at the start of every session too. Keeps the work grounded in what actually matters right now.

**Session notes** - saving what you learned at the end of each session means the next session starts with context instead of from zero. It compounds over time.

None of this is required to use Builder's Protocol. But if you want to understand how to set it up properly - hooks, project instructions, session workflows, the full picture - Jon Gerton covers all of it in his community.

**You Craft and AI Helps** - [join here (free)](https://www.skool.com/you-craft-ai-helps/about?ref=37798d7ddad04c0eba94008aa147ebed)

It is where the how lives.

---

## Credits

**Jon Gerton** - Jon-OS reviewed all six pipeline tools in March 2026. That review triggered major upgrades across the pipeline. SENTINEL's pass/fail threshold system and expanded injection attack library came directly from his findings. The session-extract knowledge workflow concept is also his. Jon runs [You Craft and AI Helps](https://www.skool.com/you-craft-ai-helps/about?ref=37798d7ddad04c0eba94008aa147ebed).

**Simon Willison** - the Lethal Trifecta check inside GUARDIAN (private user data + untrusted input + external action capability = critical security risk) is based on his work. Source: Lenny Podcast, April 2026.

---

## Philosophy

One tool. One job.

The human decides. The AI prepares.

Security is built in from the start, not added at the end.

Run GUARDIAN before any production push. Run SENTINEL on anything that has real users and AI components. Run BRAINSTORM before you build anything - ideas that skip planning usually have a scope problem.

A product that ships small and works is better than one planned perfectly and never launched.

---

*Built by [Liina Suoniemi](https://github.com/LiinaSuoniemi) / [LinkedIn](https://linkedin.com/in/liina-suoniemi) / [InkNCode Solutions](https://github.com/LiinaSuoniemi)*
