"""Arithmetic quiz using lambda functions for the calculations."""

from random import randint

add = lambda first, second: first + second
subtract = lambda first, second: first - second
multiply = lambda first, second: first * second
divide = lambda first, second: first / second
exponent = lambda first, second: first ** second
remainder = lambda first, second: first % second


def main():
    score = 0
    questions = 0
    operations = ("+", "-", "*", "/", "**", "%")

    while True:
        operation = input("Choose +, -, *, /, **, or % (or q to quit): ").strip()
        if operation.lower() == "q":
            break
        if operation not in operations:
            print("Please choose one of the listed operations.")
            continue

        number1 = randint(0, 9)
        number2 = randint(0, 9)
        if operation in ("/", "%") and number2 == 0:
            print("Division or remainder by zero is not allowed. Try again.")
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

    print(f"Final score: {score}/{questions}")


if __name__ == "__main__":
    main()
