# Builder's Protocol

An eight-tool pipeline for building AI-assisted software safely.

Built for solo developers and first-time builders who use Claude Code. Gives structure to the full build cycle - from rough idea to deployed product - with security checks at every stage.

---

## What problem this solves

When you build with AI assistance, it is easy to end up with code that works but nobody fully understands. Or code that ships before anyone checked whether it is safe. Or a half-finished idea that becomes a half-finished product because the brief was never clear.

Builder's Protocol gives you eight focused tools, each with one job, used in order. Together they cover the full journey from "I have an idea" to a product that stays safe after it ships.

---

## The pipeline

```
BRAINSTORM → CODEMAKER → VIBECODER → CODEKEEPER → GUARDIAN → SENTINEL → DEPLOY → MONITOR
```

| Step | Tool | What it does |
|------|------|-------------|
| 0 | BRAINSTORM | Turns a rough idea into a clear plan before anything gets built |
| 1 | CODEMAKER | Builds new projects from scratch - clean, safe, documented |
| 2 | VIBECODER | Scans what was built and reports what to watch out for |
| 3 | CODEKEEPER | Maintains, fixes, and extends existing code |
| 4 | GUARDIAN | Reviews everything before it goes live |
| 5 | SENTINEL | Tests AI systems for security vulnerabilities |
| 6 | DEPLOY | Pre-deployment gate. Confirms the previous tools ran and passed before anything ships |
| 7 | MONITOR | Post-deployment behavioral regression testing. Runs on a schedule after the system is live |

Each tool hands off to the next. BRAINSTORM produces a brief CODEMAKER can start from directly. VIBECODER documents what CODEMAKER built so CODEKEEPER can work safely. GUARDIAN reviews before SENTINEL tests. DEPLOY is the human confirmation gate that nothing ships without. MONITOR keeps watching after it ships.

You do not have to use all eight every time. A small fix might only need CODEKEEPER and GUARDIAN. A new project starts at BRAINSTORM. An inherited codebase starts at VIBECODER. DEPLOY runs last before code reaches users. MONITOR runs after, on a schedule.

---

## Where do I start?

**I have an idea but have not started building yet** → BRAINSTORM

**I know what to build and need to write code from scratch** → CODEMAKER

**I have code I did not write or do not fully understand** → VIBECODER

**I need to fix a bug or add a feature to existing code** → CODEKEEPER

**My code is ready and I want to check it before deploying** → GUARDIAN

**I have AI features talking to real users** → GUARDIAN then SENTINEL

**I inherited someone else's codebase** → VIBECODER to map what is there, then CODEKEEPER for fixes

**Whatever path you take, if the code is going to real users** → DEPLOY runs last before it ships. MONITOR runs after, on a schedule. Both are required.

---

## Using individual tools

You do not need the full pipeline every time. Pick the entry point that fits what you actually have in front of you.

| Situation | Tools |
|-----------|-------|
| Fix a bug in code you know well | CODEKEEPER → GUARDIAN |
| Add a feature to existing code | CODEKEEPER → GUARDIAN |
| New feature on an existing project, scope unclear | BRAINSTORM → CODEMAKER → GUARDIAN |
| Inherited a codebase, no documentation | VIBECODER → CODEKEEPER |
| Audit before a production push | GUARDIAN |
| AI system already live, want to stress-test it | SENTINEL |
| Vibe-coded project, unclear what was built | VIBECODER → GUARDIAN → SENTINEL |
| Quick idea check, not ready to build yet | BRAINSTORM only |
| Security review only, no new code | GUARDIAN → SENTINEL |
| Taking over someone else's AI project | VIBECODER → GUARDIAN → SENTINEL |
| Refactor with no new features | CODEKEEPER → GUARDIAN |
| Pre-launch audit with AI components | GUARDIAN → SENTINEL → DEPLOY |
| Pushing code to real users | DEPLOY (after previous tools passed) |

**SENTINEL** is for AI systems with real users. Standard web app, no AI features - skip it. GUARDIAN covers the rest.

**BRAINSTORM** is for when scope is unclear. If you already know exactly what to build, skip it and go straight to CODEMAKER.

**VIBECODER** is the right entry point any time you are working with code you did not write or have not read - whether that is inherited, AI-generated, or just unfamiliar.

**DEPLOY** runs last, every time. It is the human confirmation gate that the previous tools have actually run and passed before anything reaches real users. Do not skip it because the rest of the pipeline ran clean. The point of DEPLOY is the verification, not the verdict.

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
/deploy
```

**Step 4.** Verify it worked. Type `/brainstorm` in a fresh Claude Code session. If the skill activates and starts asking you questions about your idea, the install is correct. If nothing happens, check that the folder is at exactly `~/.claude/skills/brainstorm/SKILL.md` (Mac/Linux) or `C:\Users\[your-username]\.claude\skills\brainstorm\SKILL.md` (Windows) — the folder name has to match the slash command.

---

## New to Claude Code?

If you have never used Claude Code before, start with Jon Gerton's community before installing skills.

**You Craft and AI Helps** - [join here (free)](https://www.skool.com/you-craft-ai-helps/about?ref=37798d7ddad04c0eba94008aa147ebed)

Jon teaches Claude Code from the beginning - what it is, how to set it up, how to actually use it. Courses cover the basics through advanced workflows. Free to join. Once you have the basics down, come back here and the skills will make immediate sense.

---

## Configuration

Four tools have an **ADAPT THIS SECTION** block at the end of their SKILL.md file: **BRAINSTORM, CODEMAKER, CODEKEEPER, VIBECODER**. Open the file, fill in your project name, tech stack, deployment platform, and any areas that must not be changed without explicit permission. The tool reads this on every run so you do not have to repeat the context.

**GUARDIAN, SENTINEL, and DEPLOY** do not have ADAPT blocks. They run on whatever you describe to them at activation, plus the reports they read from `reviews/` (see next section).

These skills do not send email or push notifications by default. Reports are written to chat and saved to `reviews/TOOLNAME-YYYYMMDD.md`. If you want alerts when a report contains a Critical finding, wire it up yourself. Three working setups below.

### Alert on Critical findings — three options

Each option uses the same trigger: a script that scans the most recent file in `reviews/` for the word `CRITICAL` and pings you if it finds one. Pick the one that fits your stack.

**Option 1 — Slack webhook (free, 5 minutes)**

1. Create an incoming webhook at https://api.slack.com/messaging/webhooks. Copy the URL.
2. Save this as `alert.sh` in your project root:

```bash
#!/bin/bash
WEBHOOK="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
LATEST=$(ls -t reviews/*.md 2>/dev/null | head -1)
if [ -n "$LATEST" ] && grep -q CRITICAL "$LATEST"; then
  curl -X POST -H "Content-Type: application/json" \
    --data "{\"text\":\":rotating_light: Critical finding in $LATEST\"}" \
    "$WEBHOOK"
fi
```

3. Run `bash alert.sh` after each VIBECODER, GUARDIAN, or SENTINEL session.

**Option 2 — Email via Resend (free for 100 emails/day)**

1. Sign up at https://resend.com, get an API key, verify a sending domain.
2. Save as `alert.sh`:

```bash
#!/bin/bash
LATEST=$(ls -t reviews/*.md 2>/dev/null | head -1)
if [ -n "$LATEST" ] && grep -q CRITICAL "$LATEST"; then
  curl -X POST "https://api.resend.com/emails" \
    -H "Authorization: Bearer YOUR_RESEND_API_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"from\":\"alerts@yourdomain.com\",\"to\":\"you@yourdomain.com\",\"subject\":\"Critical finding in Builder's Protocol review\",\"text\":\"File: $LATEST\"}"
fi
```

3. Run after each session.

**Option 3 — Desktop notification (no third-party service)**

```bash
#!/bin/bash
LATEST=$(ls -t reviews/*.md 2>/dev/null | head -1)
if [ -n "$LATEST" ] && grep -q CRITICAL "$LATEST"; then
  # macOS
  osascript -e "display notification \"Critical in $LATEST\" with title \"Builder's Protocol\""
  # Linux
  # notify-send "Builder's Protocol" "Critical in $LATEST"
  # Windows PowerShell (requires BurntToast module)
  # New-BurntToastNotification -Text "Builder's Protocol", "Critical in $LATEST"
fi
```

Uncomment the line for your OS.

### Run it automatically

Two ways to make the alert fire without you typing the command each time.

**Claude Code hook (fires when a session ends)** — open `~/.claude/settings.json` and add a `Stop` hook that runs `bash /path/to/your/project/alert.sh`. Exact hook syntax is in Claude Code's documentation (run `/help` in your Claude Code session or check the Anthropic docs). The `update-config` skill in Claude Code can write the hook for you if you describe what you want.

**Cron job (fires on a schedule)** — add a line to your crontab to run `alert.sh` every 10 minutes:

```
*/10 * * * * cd /path/to/your/project && bash alert.sh
```

Cron is the simpler option if you do not want to deal with hook syntax.

### Hardening notes

- Add `alert.sh` to `.gitignore` if it contains your webhook URL or API key.
- Better: store secrets in environment variables and reference them in the script (`$RESEND_API_KEY`, `$SLACK_WEBHOOK`).
- The script above only catches `CRITICAL`. If you also want HIGH alerts, change `grep -q CRITICAL` to `grep -qE 'CRITICAL|HIGH'`.
- If you run multiple Builder's Protocol projects, drop the script into each project root. The `reviews/` path is project-relative.

### Make the pipeline mechanical: wire up Archon

DEPLOY enforces **human judgment**. If you also want mechanical enforcement so VIBECODER, GUARDIAN, and SENTINEL **cannot be skipped or forgotten**, wire Archon underneath.

Archon is Cole Medin's open-source harness builder. It encodes a development process as YAML workflows that are non-skippable. Repo: [github.com/coleam00/Archon](https://github.com/coleam00/Archon) (MIT license).

**Conceptual setup:**

1. Install Archon — follow the install instructions in Archon's repo (the exact command may change as the project evolves).

2. Create a workflow file in your project that defines the pipeline order. Each phase checks that the corresponding Builder's Protocol report exists in `reviews/` and passed:
   - `vibecoder-scan` — expects `reviews/VIBECODER-*.md` to exist; fail if any unresolved CRITICAL findings
   - `guardian-review` — expects `reviews/GUARDIAN-*.md`; fail if signal is RED
   - `sentinel-eval` — expects `reviews/SENTINEL-*.md`; fail if result is FAIL (only required if the project has AI components)
   - `deploy-gate` — expects `reviews/DEPLOY-LOG.md` updated for current version; fail if not GREEN

3. Configure Archon to **block any production push** if any phase is missing or failing.

4. Archon now enforces the technical pipeline mechanically. You still run DEPLOY at the end for the human judgment gate. Mechanical enforcement and human judgment are different jobs; you want both.

**Why both Archon and DEPLOY:**

Archon catches mechanical lapses (you forgot to run SENTINEL). DEPLOY catches judgment lapses (SENTINEL passed but you have not actually tested the kill switch). A clean Archon run does not mean it is safe to ship. A clean DEPLOY run after a clean Archon run does.

**Refer to Archon's documentation** for the exact YAML syntax — Archon evolves and the README's job is to point you at the right tool, not to mirror its docs. Archon's repo has install instructions, example workflows, and version-specific syntax.

---

## Review reports saved automatically

VIBECODER, CODEKEEPER, GUARDIAN, and SENTINEL save their reports to a file automatically after each run:

```
[your-project-folder]/reviews/TOOLNAME-YYYYMMDD.md
```

Every review is saved as a dated file. You build up a review history for your project over time without any extra steps.

DEPLOY appends to a single file:

```
[your-project-folder]/reviews/DEPLOY-LOG.md
```

Every successful deployment is logged with its date, version, destination, and the report dates of VIBECODER, GUARDIAN, and SENTINEL that cleared it. You build up a deployment history that maps directly to your security review history.

---

## Going further - reminders and project context

The skills work as standalone tools. No extra setup required.

But if you find yourself forgetting which tool to use next, or losing context between sessions, Claude Code has two features worth knowing about.

**Hooks** are small reminders you can set up in Claude Code's settings. They fire automatically at specific moments - at the start of a session, after each response, when a file is written. You can use them to display the pipeline order every time you open Claude Code, or to prompt yourself to run GUARDIAN before pushing code. If you are the kind of person who gets deep into building and forgets the safety steps, hooks solve that.

**Project instructions** let you write a persistent note that Claude Code reads at the start of every session. Your tech stack, your rules, which tool handles which job. You write it once in a file called `CLAUDE.md` in your project folder. Every session starts with that context already loaded - you do not have to re-explain your project each time.

**A personal context file** takes this further. Some builders keep a separate file with their current priorities, energy level, active projects, and working preferences. Claude Code can be set up to read this at the start of every session too. Keeps the work grounded in what actually matters right now.

**Session notes** - saving what you learned at the end of each session means the next session starts with context instead of from zero. It compounds over time.

None of this is required to use Builder's Protocol. But if you want to understand how to set it up properly - hooks, project instructions, session workflows, the full picture - Jon Gerton covers all of it in his community (link in the New to Claude Code section above).

---

## Credits

Specific people made specific parts better. The rest I built.

**Jon Gerton** — review of all six tools in March 2026 closed two SENTINEL gaps (pass/fail thresholds, injection library). Session-extract concept is his. Runs [You Craft and AI Helps](https://www.skool.com/you-craft-ai-helps/about?ref=37798d7ddad04c0eba94008aa147ebed).

**Nicholas Vidal** — Guardianship framing, operating logic of GUARDIAN's phases, cascade failure framing (AI fails in loops, chains, and cascades). Six operational checks across the phases: named owner with response time (Phase 6), data impact labels (Phase 2), kill-switch drill (Phase 4), misuse moment script (Phase 2), logs need an owner (Phase 5), track changes log. [nicholasvidal.tech](https://nicholasvidal.tech/)

**Cole Medin** — creator of [Archon](https://github.com/coleam00/Archon). His Dark Factory framing of mechanical pipeline enforcement showed me the pipeline needed a human gate. I built DEPLOY to be that gate. Archon and DEPLOY are different tools doing different jobs.

**Matthew Sutherland** — web content injection checks in VIBECODER, GUARDIAN and SENTINEL; concealment instruction detection ("never tell the user"); model variance note in SENTINEL. From his real-world audit findings. Founder of [ByteFlowAI](https://www.linkedin.com/in/matthew-sutherland-byteflowai/).

**Simon Willison** — Lethal Trifecta check in GUARDIAN (private user data + untrusted input + external action = critical risk). Source: Lenny's Podcast, April 2026.

**Kevin Farrugia** — "nightmare scenario in one sentence" framing for Phase 2 severity classification. Incentive problem framing (companies are rewarded for speed to market, not kill switches). [Community](https://www.skool.com/placeholder-group-6477/about).

**[Hlias Staurou](https://linkedin.com/in/hlias-staurou-a632a197)** — named the post-deployment monitoring gap. His description of ATLAS runtime verification (Ed25519-signed receipts, five-gate execution verification on every live request) made the distinction precise: pre-deployment review catches design failures, runtime verification catches execution failures. That distinction is what MONITOR is built on. Builder of AetherCode, production AI proxy with Zero-Trust AI Execution.

---

## Philosophy

One tool. One job.

The human decides. The AI prepares.

Security is built in from the start, not added at the end.

Run GUARDIAN before any production push. Run SENTINEL on anything that has real users and AI components. Run BRAINSTORM before you build anything - ideas that skip planning usually have a scope problem. Run DEPLOY last, every time. It is the gate that catches what the rest of the pipeline assumed was handled.

A product that ships small and works is better than one planned perfectly and never launched.

---

*Built by [Liina Suoniemi](https://github.com/LiinaSuoniemi) / [LinkedIn](https://linkedin.com/in/liina-suoniemi) / [InkNCode Solutions](https://github.com/LiinaSuoniemi)*
