def binary_search(number_list,target):
    number_list = sorted(number_list)
    lowest_index = 0
    highest_index = len(number_list)-1
   
    while lowest_index <= highest_index:
        middle_index = (lowest_index + highest_index) // 2 
        if number_list[middle_index] == target:
            print("got it -",number_list[middle_index]," ",middle_index)
            return True
        elif number_list[middle_index] < target:
            lowest_index = middle_index+1
        else:
            highest_index = middle_index-1

    print("no value found")
    return False

#testing out the function
binary_search([1,22,31,2,5,4,33,21,2,3,55,6,7,9888,6,5,3,2,4,56],3)
