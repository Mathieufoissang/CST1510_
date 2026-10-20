"""Print a timestamped authentication event."""

from datetime import datetime

username = input("Username: ").strip()
action = input("Action (LOGIN or LOGOUT): ").strip().upper()

if action not in ("LOGIN", "LOGOUT"):
    print("Action must be LOGIN or LOGOUT.")
else:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {action} user={username}")
