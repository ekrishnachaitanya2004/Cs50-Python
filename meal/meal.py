def main():
    input_time = input("What time is it? ")

    hours = convert(input_time)
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0: 
        print("dinner time")

def convert(input_time):
    if "a.m." in input_time or "p.m." in input_time:
        input_time, period = input_time.strip().split()

        hours, minutes = input_time.split(":")
        hours = int(hours)
        minutes = int(minutes)

        if period == "p.m." and hours != 12:
            hours += 12
        elif period == "a.m." and hours == 12:
            hours = 0
    else:
        hours, minutes = input_time.split(":")
        hours = int(hours)
        minutes = int(minutes)

    return hours + minutes / 60

if __name__ == "__main__":
    main()
