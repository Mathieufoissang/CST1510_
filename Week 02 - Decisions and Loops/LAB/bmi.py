"""Calculate BMI from weight in pounds and height in inches."""

weight_pounds = float(input("Enter weight in pounds: "))
height_inches = float(input("Enter height in inches: "))

if height_inches <= 0 or weight_pounds <= 0:
    print("Weight and height must be greater than zero.")
else:
    weight_kg = weight_pounds * 0.45359237
    height_m = height_inches * 0.0254
    bmi = weight_kg / (height_m ** 2)

    print(f"BMI is {bmi:.1f}")
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25.0:
        print("Normal")
    elif bmi < 30.0:
        print("Overweight")
    else:
        print("Obese")
