def check_age_range(age):
    """
    Checks if an age is within the range of 10 to 20 (inclusive) using nested conditional statements.
    """
    if age >= 10:
        if age <= 20:
            print("Age is within the range (10-20) you can yse this App.")
        else:
            print("Age is greater than 20 you can use this app.")
    else:
        print("Age is less than 10, Sorry can't use this app.")


try:
    age = int(input("Enter your age: "))
    check_age_range(age)
except ValueError:
    print("Invalid input. Please enter a valid number for age or can't use this app.")