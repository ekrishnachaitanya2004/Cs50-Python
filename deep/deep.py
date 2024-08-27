user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
converted_input = user_input.lower().strip()
if converted_input == "42" or converted_input == "forty two" or converted_input == "forty-two":
    print("Yes")
else:
    print("No")
