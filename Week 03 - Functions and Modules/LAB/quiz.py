"""Practise arithmetic with randomly generated single-digit numbers."""

from random import randint


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


def exponent(number1, number2):
    return number1 ** number2


def remainder(number1, number2):
    return number1 % number2


def main():
    score = 0
    questions = 0
    keep_practising = True

    while keep_practising:
        print("\nChoose an operation: +, -, *, /, **, %")
        operation = input("Operation: ").strip()
        if operation not in ("+", "-", "*", "/", "**", "%"):
            print("Please choose one of the listed operations.")
            continue

        number1 = randint(0, 9)
        number2 = randint(0, 9)
        if operation in ("/", "%") and number2 == 0:
            print("Division or remainder by zero is not allowed. Try another question.")
            continue

        if operation == "+":
            answer = add(number1, number2)
        elif operation == "-":
            answer = subtract(number1, number2)
        elif operation == "*":
            answer = multiply(number1, number2)
        elif operation == "/":
            answer = divide(number1, number2)
        elif operation == "**":
            answer = exponent(number1, number2)
        else:
            answer = remainder(number1, number2)

        user_answer = float(input(f"What is {number1} {operation} {number2}? "))
        questions += 1
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The answer is {answer:g}.")

        print(f"Score: {score}/{questions}")
        keep_practising = input("Would you like another question? (y/n): ").lower() == "y"

    print(f"Final score: {score}/{questions}")


if __name__ == "__main__":
    main()
