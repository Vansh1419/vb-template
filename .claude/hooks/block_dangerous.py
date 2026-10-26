import json, re, sys

cmd = json.load(sys.stdin).get("tool_input", {}).get("command", "")

BLOCKED = [
    r"\brm\s+-[a-z]*r[a-z]*f|\brm\s+-[a-z]*f[a-z]*r",  # rm -rf / rm -fr
    r"git\s+push\s+.*(--force|-f\b)",
    r"git\s+reset\s+--hard",
    r"git\s+clean\s+-[a-z]*f",
    r"\bsudo\b",
    r"\bmkfs\b|\bdd\s+if=",
    r"curl[^|]*\|\s*(ba)?sh|wget[^|]*\|\s*(ba)?sh",
    r"\bchmod\s+-R\s+777",
]

for pattern in BLOCKED:
    if re.search(pattern, cmd):
        print(f"Blocked dangerous command: {cmd}\nAsk the user to run it themselves.", file=sys.stderr)
        sys.exit(2)
