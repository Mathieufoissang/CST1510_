"""Convert human years to dog years using the exercise's rule."""

human_years = float(input("Enter the dog's age in human years: "))

if human_years < 0:
    print("Age cannot be negative.")
elif human_years <= 2:
    dog_years = human_years * 10.5
    print(f"{human_years:g} human years is {dog_years:g} dog years.")
else:
    dog_years = 2 * 10.5 + (human_years - 2) * 4
    print(f"{human_years:g} human years is {dog_years:g} dog years.")
