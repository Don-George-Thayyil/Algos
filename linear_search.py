def sorted_linear_search(victim,target):
    target = sorted(target)
    n = len(target)
    for i in target:
        if i == victim:
            return True
        elif i >victim:
            print(i,"damn")
            break
    return False


sorted_linear_search(4,[7,2,3,5,6,9,0])
