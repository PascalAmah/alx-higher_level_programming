#!/usr/bin/python3

def uniq_add(my_list=[]):

    uniq_set = set()
    for num in my_list:
        uniq_set.add(num)
    sum_uniq_set = sum(uniq_set)
    return sum_uniq_set
