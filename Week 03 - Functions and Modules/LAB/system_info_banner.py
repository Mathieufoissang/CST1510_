"""Display the host name, operating system, and Python version."""

import platform

hostname = input("Hostname: ").strip()
print(f"Host: {hostname}")
print(f"OS: {platform.system()}")
print(f"Python: {platform.python_version()}")
