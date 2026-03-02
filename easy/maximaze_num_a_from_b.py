# Даны два строковых представления чисел A и B. Нужно максимизировать A, 
# заменив в нём любую цифру на цифру из B. Каждую цифру B можно использовать только один раз.

def str_to_int_list(s : str) -> list:
    return [int(i) for i in s]

def maximaze_num_a_from_b(a: str, b: str) -> str:
    dig_a = str_to_int_list(a)
    dig_b = sorted(str_to_int_list(b))

    for i in range(len(dig_a)):
        if dig_b == []:
            break
        if dig_a[i]< dig_b[-1]:
            dig_a[i] = dig_b.pop()

    return "".join(str(i) for i in dig_a)

a = "955599"
b = "11"

print(maximaze_num_a_from_b(a, b))    