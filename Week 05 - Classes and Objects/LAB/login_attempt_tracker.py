"""Cyber: Login Attempt Tracker

Create an Account with username, password, and failed_attempts. login(password)
returns True for a correct password and resets failed attempts; incorrect
passwords increase the count. After 3 failed attempts, lock the account and
refuse every later login. Test both correct and incorrect passwords.
"""


class Account:
    MAX_FAILED_ATTEMPTS = 3

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.failed_attempts = 0

    @property
    def is_locked(self):
        return self.failed_attempts >= self.MAX_FAILED_ATTEMPTS

    def login(self, password):
        if self.is_locked:
            print(f"Login refused: account '{self.username}' is locked.")
            return False

        if password == self.password:
            self.failed_attempts = 0
            print("Login successful.")
            return True

        self.failed_attempts += 1
        print(f"Incorrect password ({self.failed_attempts} failed attempt(s)).")
        if self.is_locked:
            print(f"Account '{self.username}' is now locked.")
        return False


account = Account("student01", "correct-horse")
account.login("wrong-one")
account.login("wrong-two")
account.login("correct-horse")  # A successful login resets the failure count.
account.login("wrong-three")
account.login("wrong-four")
account.login("wrong-five")  # The third consecutive failure locks the account.
account.login("correct-horse")  # Even the right password is refused while locked.
