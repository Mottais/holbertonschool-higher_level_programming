#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    poid = 0
    pond = 0

    for i in my_list:
        poid += i[0] * i[1]
        pond += i[1]
    return poid / pond
