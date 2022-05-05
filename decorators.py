import datetime


def decorator_maker(filepath: str):
    def my_decorator(decorated_function):
        def wrapper_function(*args, **kwargs):
            result = decorated_function(*args, **kwargs)
            with open(filepath, mode='a', encoding='utf8') as f:
                f.write(f'Дата и время вызова: {datetime.datetime.today()} Имя: {decorated_function.__name__} '
                        f'Результат: {result} Аргументы: {args} {kwargs}\n')

            return result

        return wrapper_function

    return my_decorator
