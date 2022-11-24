def hello():
    print("Hello, World!")


def get_name():
    print("Как тебя зовут?")
    name = input()
    return name


if __name__ == '__main__':
    hello()
    name = get_name()
    print(f"Добро пожаловать, {name}!")