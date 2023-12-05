#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_new = []
    for number in my_list:
        if (number % 2) == 0:
            list_new.append(True)
        else:
            list_new.append(False)
    return(list_new)
