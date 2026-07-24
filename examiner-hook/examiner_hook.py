#!/usr/bin/env python3
"""
EXAMINER detection hook.

Idea credit: Ivett Ordog, Habit Hooks (https://github.com/devill/habit-hooks).

The principle: a deterministic linter finds a cheap proxy that correlates with
AI slop. It does not need to be bulletproof. The linter only points; the
agent (or human) reacts to the specific issue, and can ignore false positives.
Instead of printing a bare metric ("function is too complex"), this hook
delivers the behavioral prompt right at the smell, so the guidance sits next
to the code it is about, not in a rule far back in the conversation.

Two ways to run:

  1. By hand (the demo, or a manual EXAMINER pass):
         python examiner_hook.py <path> [<path> ...]
     Prints a human-readable list of smells and their coaching prompts.

  2. As a Claude Code PostToolUse hook (the always-on guard):
         python examiner_hook.py --hook
     Reads the tool call as JSON on stdin, checks the file that was just
     edited, and if it smells, prints the coaching prompt as PostToolUse
     additionalContext so it reaches the agent's next reasoning step. Silent
     (exit 0) on clean edits, non-Python files, or any error. It never blocks
     the edit: it informs, it does not undo.
"""
import json
import os
import subprocess
import sys

# Each deterministic ruff rule maps to the behavioral prompt EXAMINER wants
# acted on, delivered at the smell.
PROMPTS = {
    "C901": (
        "Write in one sentence what this function does. Refactor until the code "
        "reads as close to that sentence as possible. If you cannot say it in "
        "one sentence, it has more than one responsibility."
    ),
    "BLE001": (
        "This catches every error. Name the specific exception you expect, and "
        "make sure the failure is logged or surfaced, never silently swallowed. "
        "A swallowed error is a bug you will debug blind later."
    ),
}


def detect(paths):
    """Run the ruff smell checks on paths and return the list of findings.

    Returns a list of ruff finding dicts (empty list = clean). Returns None if
    ruff could not be run or its output could not be parsed, so callers can
    tell "clean" apart from "could not check"."""
    cmd = [
        sys.executable, "-m", "ruff", "check", *paths,
        "--select", ",".join(PROMPTS),
        "--config", "lint.mccabe.max-complexity=5",
        "--no-cache", "--output-format", "json",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
    except OSError:
        return None
    try:
        return json.loads(result.stdout or "[]")
    except json.JSONDecodeError:
        return None


def describe(finding):
    """Turn one ruff finding into (location, code, message, coaching prompt)."""
    code = finding.get("code")
    loc = f"{os.path.basename(finding['filename'])}:{finding['location']['row']}"
    message = finding.get("message", "")
    prompt = PROMPTS.get(code, "Review this.")
    return loc, code, message, prompt


def run_cli(paths):
    """Manual mode: print smells and prompts for a human reading the terminal."""
    findings = detect(paths)
    if findings is None:
        print("Could not run ruff. Is it installed? (pip install ruff)")
        return
    if not findings:
        print("No smells detected. Nothing to react to.")
        return
    for finding in findings:
        loc, code, message, prompt = describe(finding)
        print(f"\n  {loc}  [{code}]")
        print(f"  detected: {message}")
        print(f"  -> {prompt}")
    print()


def run_hook():
    """PostToolUse mode: read stdin JSON, coach on the edited file if it smells.

    Always exits 0. Prints the coaching prompt as additionalContext only when
    the edited Python file smells; prints nothing otherwise. A hook that errored
    or blocked would interrupt the session, so every failure path stays silent."""
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return
    tool_input = event.get("tool_input") or {}
    # Edit / Write / MultiEdit put the edited file in file_path. Fall back to
    # path in case a future tool uses that name.
    path = tool_input.get("file_path") or tool_input.get("path")
    if not path or not path.endswith(".py") or not os.path.isfile(path):
        return
    findings = detect([path])
    if not findings:  # None (ruff failed) or [] (clean) -> say nothing
        return
    blocks = []
    for finding in findings:
        loc, code, message, prompt = describe(finding)
        blocks.append(f"{loc} [{code}] {message}\n  -> {prompt}")
    context = (
        "EXAMINER hook flagged smells in the file you just edited. Fix the root "
        "cause, do not suppress the warning:\n\n" + "\n\n".join(blocks)
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": context,
        }
    }))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--hook":
        run_hook()
        sys.exit(0)
    if not args:
        print("Usage: python examiner_hook.py <path> [<path> ...]"
              "   (or --hook to run as a PostToolUse hook)")
        sys.exit(1)
    run_cli(args)
