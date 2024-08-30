def main():
    grocery_list = {}
    while True:
        try:
            item = input().strip().upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            break
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")

main()
