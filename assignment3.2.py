score = float(input("Enter your score: "))

if 0 <= score <= 100:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"The grade is {grade}")
else:
    print("Error, please enter numeric input between 0 and 100")
