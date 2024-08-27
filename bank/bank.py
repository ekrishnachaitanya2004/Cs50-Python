pay = ()
user_input = input("Greeting: ")
x = user_input.split()
y = (x[0]).lower()
if y == "hello" or y =="hello,":
    pay = 0
elif y[0] == "h":
    pay = 20
else:
    pay = 100
print(f"${pay}")
