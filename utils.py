def find_max(num_list):
    max_num = num_list[0]
    for i in num_list:
        if i > max_num:
            max_num = i
    return max_num
