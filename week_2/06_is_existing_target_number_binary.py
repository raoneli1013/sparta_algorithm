finding_target = 2
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    while array:
        avg_num = len(array)//2
        if target > array[avg_num]:
            array = array[array[avg_num]+1:]
        elif target < array[avg_num]:
            array = array[:array[avg_num]]
        else:
            return True
    return False




result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)