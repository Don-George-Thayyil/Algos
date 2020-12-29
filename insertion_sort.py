def insertion_sort(number_list):
    length = len(number_list)
    for i in range(1,length):
        value = number_list[i]
        position = i
        while position > 0 and value < number_list[position- 1]:
            number_list[position] = number_list[position - 1]
            position -= 1 
        number_list[position] = value
    print(number_list)

number_list = [1,24,2,12,34,5,3,3,45,67,4578,3434,4323,2,4,21,3,2,3,4,5,9]

insertion_sort(number_list)
