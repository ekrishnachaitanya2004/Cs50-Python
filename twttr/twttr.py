def main():
    user_input = input("Input: ")
    result = remove_vowels(user_input)
    print(result)


def remove_vowels(user_input):
    vowels = "AEIOUaeiou"
    return ''.join([char for char in user_input if char not in vowels])


if __name__ == "__main__":
    main()
