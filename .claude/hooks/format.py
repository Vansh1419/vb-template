import json, os, shutil, subprocess, sys

path = json.load(sys.stdin).get("tool_input", {}).get("file_path", "")
ext = os.path.splitext(path)[1].lower()

# Runs a formatter only if it is installed. Add more as needed.
FORMATTERS = {
    (".py",): ["ruff", "format"],
    (".js", ".jsx", ".ts", ".tsx", ".json", ".css", ".html", ".md"): ["prettier", "--write"],
    (".go",): ["gofmt", "-w"],
    (".rs",): ["rustfmt"],
}

for exts, cmd in FORMATTERS.items():
    if ext in exts and shutil.which(cmd[0]):
        subprocess.run(cmd + [path], capture_output=True)
        break
