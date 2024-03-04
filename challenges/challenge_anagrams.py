def sorted_merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = sorted_merge(left)
    right = sorted_merge(right)

    return merge(left, right)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def is_anagram(first_string, second_string):
    first_string_sorted = sorted_merge(list(first_string.lower()))
    second_string_sorted = sorted_merge(list(second_string.lower()))
    first_result_str = "".join(first_string_sorted)
    second_result_str = "".join(second_string_sorted)

    return (
        first_result_str,
        second_result_str,
        first_result_str == second_result_str
        and first_result_str != ""
        and second_result_str != "",
    )


retorno = is_anagram('ae', 'ea')
print(retorno)
