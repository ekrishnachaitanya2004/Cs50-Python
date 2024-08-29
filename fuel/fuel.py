def main():
    value_1 = ""
    while True:
        try:
            x, y = input("Fraction: ").split('/')
            x=int(x)
            y=int(y)
            value_is = round(float((x / y) * 100))
            if 0 <= value_is <= 100:
                if value_is <= 1 :
                    value_1 = "E"
                    break
                elif value_is >= 99 :
                    value_1 = "F"
                    break
                else:
                    value_1 = str(value_is)
                    value_1 += "%"
                    break
        except (ValueError,ZeroDivisionError):
            continue
    print(f"{value_1}")

main()
