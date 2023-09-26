total = 0
count = 0

while True:
    try:
        user_input = input("Enter a number or enter 'done' to finish: ")

        if user_input.lower() == 'done':
            break
        number = int(user_input)

        total += number
        count += 1

    except ValueError:
        print("Error: Invalid input. Please enter a number or 'done'.")
if count > 0:
    average = total / count
    print(f"Sum of input numbers: {total}")
    print(f"Number of inputs: {count}")
    print(f"Average of input number: {average}")
else:
    print("No valid numbers were entered.")
