
dict_1 = {num: num * 'f' for num in range(1, 6)}  # генерируем словарь


def reverse(data: dict) -> dict:
    new_dict = {value: key for key, value in data.items()}
    return new_dict


print(reverse(dict_1))
