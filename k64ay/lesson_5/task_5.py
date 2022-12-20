def check_num_str(value: str):
    dot_count = 0
    if value[0] == '-':
        neg_sign = True
        line = value[1:]
    else:
        neg_sign = False
        line = value

    for char in line:
        if char == '.':
            dot_count += 1

            if dot_count > 1:
                return "Incorrect num"
            continue

        if char == '-' or not char.isdigit():
            return "Incorrect num"

    return f"{'отрицательное' if neg_sign else 'положительное'} {'дробное' if dot_count else 'целое'} число"


print(check_num_str(input()))
