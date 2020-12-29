def selection_sort(number_list):
    length = len(number_list)
    for i in range(length-1):
        index = i
        for j in range(i+1,length):
            if number_list[j]<number_list[index]:
                index = j
        if index != i:
            temp = number_list[i]
            number_list[i] = number_list[index]
            number_list[index] = temp

    print(number_list)


nums = [1,6,4,2,3,1,5,8,4,3,9,0,7,6,2,34,21,56,765,334,2,1]

selection_sort(nums)
