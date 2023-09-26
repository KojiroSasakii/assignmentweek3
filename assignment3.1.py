try:
    hours = int(input("Enter the hours: "))
    rate = float(input("Enter the rate: "))

    if hours > 40:
        salary = 40 * rate + (hours - 40) * (1.5 * rate)
    else:
        salary = hours * rate

    print(f"Your salary is: ${salary:.2f}")

except ValueError as e:
    print("Error! Invalid input. Please enter an integer value")
except Exception as e:
    print(f"An error occurred: {e}")
