# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        return "OVER LIMIT" if self.value > self.limit else "OK"
    def __str__(self):
        return f"Record({self.label}, value={self.value}, limit={self.limit})"


r = Record("R-001", 120.0, 100.0)

r2 = Record("R-002", 80.0, 100.0)
print(r.status())
print(r2.status())
print(r)
print(r2)

