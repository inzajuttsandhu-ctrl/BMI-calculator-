print("=== BMI Calculator ===")

while True:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (meters): "))

    bmi = weight / (height * height)

    print("\nYour BMI is:", round(bmi, 2))

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

    choice = input("\nDo you want to calculate again? (y/n): ")

    if choice.lower() != "y":
        print("Thank you for using BMI Calculator 😊")
        break
