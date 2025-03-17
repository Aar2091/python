def find_square_root(number, tolerance=0.001):
    if number < 0:
        return "Cannot calculate square root of a negative number"
    
    guess = number / 2.0 
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2.0
    return guess

number = float(input("Enter a number: "))
result = find_square_root(number)
print("Square root of", number, "is approximately", result)