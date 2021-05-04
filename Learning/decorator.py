def new_decorator(original_func):
    def wrap_func():
        print('Деякий код, який виконується ДО функції original_func')

        original_func()

        print('Деякий код, який виконується ПІСЛЯ функції original_func')

    return wrap_func


@new_decorator
def func_needs_decorator():
    print('Ця функція потребує декоратора')


# decorated_func = new_decorator(func_needs_decorator)

print(func_needs_decorator())
