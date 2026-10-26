import json, os, re, sys

path = json.load(sys.stdin).get("tool_input", {}).get("file_path", "")
name = os.path.basename(path)

# .env, .env.local etc. are protected; .env.example is allowed
if re.match(r"^\.env(\..+)?$", name) and name != ".env.example" or re.search(r"\.(pem|key)$|secret", name, re.I):
    print(f"Blocked edit to secret file: {path}\nAsk the user to edit it themselves.", file=sys.stderr)
    sys.exit(2)
