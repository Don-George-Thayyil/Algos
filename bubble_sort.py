def bubble_sort(number_list):
    comparable = 0
    for i in range(len(number_list)):
        for j in range(len(number_list)-1):
            if number_list[j] > number_list[j+1]:
                temp = number_list[j]
                number_list[j] = number_list[j+1]
                number_list[j+1] = temp


    print(number_list)


#testing out the function
lis = [100,2,3,2,1,5,6,32,1,23,5,74,20,4,322,1212,56,46,32,325654,23]

bubble_sort(lis)
            
