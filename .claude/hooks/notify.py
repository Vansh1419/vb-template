import json, platform, subprocess, sys

data = json.load(sys.stdin)
msg = (data.get("message") or sys.argv[1]).replace('"', "").replace("'", "")
title = "Claude Code"
os_name = platform.system()

if os_name == "Darwin":
    subprocess.run(["osascript", "-e", f'display notification "{msg}" with title "{title}" sound name "Glass"'])
elif os_name == "Linux":
    subprocess.run(["notify-send", title, msg])
    subprocess.run(["paplay", "/usr/share/sounds/freedesktop/stereo/complete.oga"], stderr=subprocess.DEVNULL)
elif os_name == "Windows":
    ps = (
        "Add-Type -AssemblyName System.Windows.Forms;"
        "$n=New-Object System.Windows.Forms.NotifyIcon;"
        "$n.Icon=[System.Drawing.SystemIcons]::Information;$n.Visible=$true;"
        f"$n.ShowBalloonTip(5000,'{title}','{msg}','Info');"
        "[System.Media.SystemSounds]::Asterisk.Play();Start-Sleep 5;$n.Dispose()"
    )
    subprocess.run(["powershell", "-NoProfile", "-Command", ps])
