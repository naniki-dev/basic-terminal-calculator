def main():
    print("This is a basic terminal calculator. You can only + - x / two sets of digits.")

    while True:

        sign = input("Wyd? (+ - x /) or enter 'q' to quit/exit. \n> ").lower()

        if sign == "q":
            print("Bye!")
            break

        if sign == "+":
            print(f"Answer: {add(first_num(),sec_num())}")
            break
        elif sign == "-":
            print(f"Answer: {minus(first_num(),sec_num())}")
            break
        elif sign == "/":
            print(f"Answer: {divide(first_num(),sec_num())}")
            break
        elif sign == "*":
            print(f"Answer: {times(first_num(),sec_num())}")
            break
        else:
            print("Enter a valid operator.")

def first_num():
    while True:
        try:
            num = int(input("Enter your first number: "))
            if not isinstance(num, int):
                raise ValueError
            else:
                return num
        except ValueError:
            print("Only enter numbers.")

def sec_num():
    while True:
        try:
            num = int(input("Enter your second number: "))
            if not isinstance(num, int):
                raise ValueError
            else:
                return num
        except ValueError:
            print("Only enter numbers.")

def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def times(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "You cannot divide by zero"
    return x / y


if __name__ == "__main__":
    main()