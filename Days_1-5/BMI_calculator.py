import math

print("\n*** BMI Calculator ***")

height = float(input("Enter your height: "))
weight = float(input("Enter you weight: "))

float_height = round(height, 2)
float_weight = round(weight, 2)

bmi = float_weight / float_height ** 2


if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}, you are normal weigth.")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi}, you are overweigth.")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")