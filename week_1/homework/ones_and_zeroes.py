input = "0111100"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # count number of 1s and 0s.
    # if number of 1 > number 0, flip all 0 to 1
    if string.count("1") >= string.count("0"):
        # flip 0 to 1
        print("more 1 or equal")
        string = string.replace("0", "1")
        return string

    else:
        print("more 0")
        string = string.replace("1", "0")
        return string

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)