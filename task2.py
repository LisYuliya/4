# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def create_dict_from_kwargs(**kwargs):
    result_dict = {}

    for key, value in kwargs.items():
        if isinstance(value, (int, float, str, bytes)):
            result_dict[value] = key
        else:
            result_dict[str(value)] = key

    return result_dict


result = create_dict_from_kwargs(a=1, b="hello", c=[1, 2, 3], d=None, answer=42)
print(result)
