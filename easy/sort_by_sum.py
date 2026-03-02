#Отсортировать числа в массиве согласно сумме их цифр.


def sum_digit_in_num(num: int):
    return sum(int(i) for i in str(num))

def sort_list_by_sum_digit_in_num(input_list:list) -> list:
    return sorted(input_list, key = sum_digit_in_num)

test_list = [123, 45, 67, 2]
result_list = sort_list_by_sum_digit_in_num(test_list)
print(result_list)


