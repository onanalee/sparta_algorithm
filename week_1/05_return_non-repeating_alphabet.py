input = "abacabade"
input2 = "tgtgtgtgjj"


def find_not_repeating_character(string):
    #문자열에서 반복되지 않는 첫번째 알파벳을 반환해라. 만약 그런 문자가 없다면 _를 반환해라
    alphabet_array = [0] * string.len()
    print(alphabet_array)
    # for alphabet in string:
    #     for alphabet2 in string:
    #         if not alphabet == alphabet2:
    #             return alphabet




result = find_not_repeating_character(input)
print(result)