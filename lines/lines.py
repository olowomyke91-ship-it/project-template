import sys


def main():
    # 1. Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # 2. Check if the file ends with .py
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    # 3. Open the file and count lines of code
    try:
        with open(sys.argv[1], "r") as file:
            line_count = 0
            for line in file:
                stripped = line.lstrip()
                # Ignore blank lines and comments
                if stripped and not stripped.startswith("#"):
                    line_count += 1
            print(line_count)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
