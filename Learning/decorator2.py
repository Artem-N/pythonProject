passw = input("Введіть пароль: ")


def test_passw(p):
    def deco(f):
        if p == "10":
            return f
        else:
            return lambda: "Доступ закритий"

    return deco


@test_passw(passw)
def func():
    return "Доступ відкрито"


print(func())
