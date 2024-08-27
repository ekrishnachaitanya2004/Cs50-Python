result = 0
user_input = input("Expression: ")
x, y, z = user_input.split()

x = int(x)
z = int(z)
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
print(f"{float(result)}")
