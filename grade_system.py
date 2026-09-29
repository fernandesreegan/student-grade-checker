print("=" * 50)
print("             STUDENT GRADE CHECKER")
print("=" * 50)

while True:
    # Keep asking until a valid mark is entered
    while True:
        try:
            mark = float(input("\nEnter your mark (0 - 100): "))

            if 0 <= mark <= 100:
                break

            print("Invalid mark. Please enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Determine the grade
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "E"

    # Display the result
    print("\n" + "-" * 50)
    print(f"A mark of {mark:g} falls under Grade {grade}.")
    print("-" * 50)

    # Ask whether the user wants to continue
    while True:
        choice = input("\nWould you like to check another mark? (Y/N): ").strip().lower()

        if choice in ("y", "yes"):
            break
        elif choice in ("n", "no"):
            print("\nThank you for using the Student Grade Checker!")
            exit()
        else:
            print("Please enter Y for Yes or N for No.")