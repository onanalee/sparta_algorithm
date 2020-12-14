input = [3, 5, 6, 1, 2, 4]


# def is_number_exist(number, array):
#     count = 0
#     for num in array:
#         if num == number:
#             count = count + 1
#         if count > 0:
#             return True
#         else: return False

def is_number_exist(number, array):
    count = 0
    for num in array:
        if num == number:
            return True

    return False



result = is_number_exist(11, input)
print(result)