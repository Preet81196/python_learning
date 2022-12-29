def common_items(list1, list2):
    common_list = []
    for i in list1:
        if i in list2:
            common_list.append(i)
    return common_list

list1 = [1, 2,8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(common_items(list1, list2))
