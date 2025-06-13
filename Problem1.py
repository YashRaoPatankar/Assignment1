n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
add = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2 if n2 != 0 else "undefined (division by zero)"
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {multi}")
print(f"Division: {div}")