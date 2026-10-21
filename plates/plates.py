def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length must be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 3: No periods, spaces, or punctuation allowed
    if not s.isalnum():
        return False

    # Rule 4: Numbers must come at the end, and the first number cannot be '0'
    i = 0
    while i < len(s):
        if s[i].isdigit():
            # First number used cannot be '0'
            if s[i] == "0":
                return False
            # Once a number starts, all remaining characters must be digits
            while i < len(s):
                if not s[i].isdigit():
                    return False
                i += 1
        i += 1

    return True


if __name__ == "__main__":
    main()
