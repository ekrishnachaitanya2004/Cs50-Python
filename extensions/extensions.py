user_input = input("File name: ")
a = user_input.replace("."," ").split()
b = a[(len(a))-1].lower()
if b == "gif" or b == "png":
    print(f"image/{b}")
elif b == "jpg" or b == "jpeg":
    print("image/jpeg")
elif  b == "pdf" or b == "zip":
    print(f"application/{b}")
elif  b == "txt":
    print(f"text/{a[0]}")
else:
    print("application/octet-stream")
