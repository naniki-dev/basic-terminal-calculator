def main():
    print("This is a basic terminal calculator. You can only + - x / two sets of digits.")
    sign = operator_check()
    # num_1 = first_num()
    # num_2 = sec_num()
    if sign == "+":
        add()
    elif sign == "-":
        minus()
    elif sign == "/":
        divide()
    elif sign == "*":
        times()
    # else:
    #     print("Enter a valid operator.")



def first_num():
    try:
        num = int(input("Enter the first number: "))
        if not isinstance(num, int):
            raise ValueError
    except ValueError:
        print("Only enter numbers.")


def operator_check():
    while True:
        n = input("Wyd? (+ - x /) \n")
        if n in ["+", "-", "/","*"]:
            return n
        else:
            return "Enter a valid operator."


def sec_num(n):
    second = input("Enter the second number: ")


def add(x, y):
    return x + y


def minus(x, y):
    pass


def times(x, y):
    pass


def divide(x, y):
    pass


if __name__ == "__main__":
    main()