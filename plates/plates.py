def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (
        starts_with_two_letters(s) and
        is_correct_length(s) and
        has_no_invalid_characters(s) and
        numbers_at_the_end(s)
    )

def starts_with_two_letters(s):
    return len(s) >= 2 and s[0:2].isalpha()

def is_correct_length(s):
    return 2 <= len(s) <= 6

def has_no_invalid_characters(s):
    return s.isalnum()

def numbers_at_the_end(s):
    found_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0' and not found_number:
                return False
            if not s[i:].isdigit():
                return False
            found_number = True
    return True

main()
