"""Check whether text reads the same forwards and backwards."""


def is_palindrome(text):
    return text == text[::-1]


if __name__ == "__main__":
    word = input("Enter a word: ")
    if is_palindrome(word):
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
