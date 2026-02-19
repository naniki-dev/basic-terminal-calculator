def main():
    print("This is a basic terminal calculator. You can only + - x / two sets of digits.")
    sign = operator()
    num_1 = first_num()
    num_2 = sec_num()
    return num_1, sign, num_2



def first_num(n):
    first = input("Enter the first number: ")


def operator(n):
    operator = input("Wyd? + - x /")


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