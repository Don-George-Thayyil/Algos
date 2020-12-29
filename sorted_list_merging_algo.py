def sort_merge(number_list1,number_list2):
    a = 0
    b = 0
    new_list = list()
    while a<len(number_list1) and b<len(number_list2):
        if number_list1[a] < number_list2[b]:
            new_list.append(number_list1[a])
            a += 1
        else:
            new_list.append(number_list2[b])
            b += 1
    while a<len(number_list1):
        new_list.append(number_list1[a])
        a += 1
    while b < len(number_list2):
        new_list.append(number_list2[b])
        b += 1

    print(new_list)


list_1 = [1,2,3,4,5]
list_2 = [3,4,4,5,6,7,7,7,8]

sort_merge(list_1,list_2)
