input = "hello my name is sparta"
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    ## assign alphabet to [number]
    for char in string:
        if not char.isalpha():
            continue
        array_index = ord(char) - ord('a')
        alphabet_occurence_array[array_index] += 1

    max_occurence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index





    print(ord('a'))  # 97
    print(ord('a') - ord('a'))  # 97-97 -> 0
    print(ord('b') - ord('a'))  # 98-97 -> 1





    return alphabet_occurrence_array


print(find_alphabet_occurrence_array(input))