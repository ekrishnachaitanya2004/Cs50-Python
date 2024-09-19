months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if date.count("/") != 0:
            mm, dd, yy = date.split("/")
            if int(mm) > 12 or int(dd) > 31:
                continue
            print(f"{int(yy)}-{int(mm):02}-{int(dd):02}")
            break
        elif date.count(",") != 0:
            mm, dd, yy = date.split(" ")
            dd = dd.strip(",")
            if int(dd) > 31:
                continue
            mm = mm.title()
            print(f"{int(yy)}-{(months.index(mm) + 1):02}-{int(dd):02}")
            break
        else:
            continue
    except (ValueError, KeyError):
        continue
