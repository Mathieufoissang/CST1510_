"""Compose a single Apache-style HTTP log line from user input."""

ip_address = input("IP address: ")
method = input("HTTP method: ")
path = input("Path: ")
status = input("Status code: ")
bytes_sent = input("Bytes sent: ")

print(f'{ip_address} - "{method} {path}" {status} {bytes_sent}')
