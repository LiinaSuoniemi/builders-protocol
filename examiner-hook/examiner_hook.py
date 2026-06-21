#!/usr/bin/env python3
"""
EXAMINER detection hook (prototype).

Idea credit: Ivett Ordog, Habit Hooks (https://github.com/devill/habit-hooks).

The principle: a deterministic linter finds a cheap proxy that correlates with
AI slop. It does not need to be bulletproof. The linter only points; the
agent (or human) reacts to the specific issue, and can ignore false positives.
Instead of printing a bare metric ("function is too complex"), this hook
delivers the behavioral prompt right at the smell, so the guidance sits next
to the code it is about, not in a rule far back in the conversation.

Usage:
    python examiner_hook.py <path> [<path> ...]
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


def main(paths):
    cmd = [
        sys.executable, "-m", "ruff", "check", *paths,
        "--select", ",".join(PROMPTS),
        "--config", "lint.mccabe.max-complexity=5",
        "--no-cache", "--output-format", "json",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    try:
        findings = json.loads(result.stdout or "[]")
    except json.JSONDecodeError:
        print(result.stdout or result.stderr)
        return

    if not findings:
        print("No smells detected. Nothing to react to.")
        return

    for f in findings:
        code = f.get("code")
        loc = f"{os.path.basename(f['filename'])}:{f['location']['row']}"
        detected = f.get("message", "")
        prompt = PROMPTS.get(code, "Review this.")
        print(f"\n  {loc}  [{code}]")
        print(f"  detected: {detected}")
        print(f"  -> {prompt}")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python examiner_hook.py <path> [<path> ...]")
        sys.exit(1)
    main(sys.argv[1:])
