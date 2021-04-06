if __name__ == "__main__":
    first_list = [i for i in range(1, 6)]
    second_list = [i for i in range(-3, 9)]
    result_list = first_list + second_list
    result_list_new = list()

    for item in result_list:
        if item not in result_list_new:
            result_list_new.append(item)

    result_list_new = sorted(result_list_new)

    result_list_1 = list()
    for i in range(len(result_list_new) - 1, -1, -1):
        result_list_1.append(result_list_new[i])
