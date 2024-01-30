#!/usr/bin/python3
def search_replace(my_list, search, replace):

    my_new_list = list(my_list)

    for i in range(len(my_new_list)):
        if my_new_list[i] == search:
            my_new_list[i] = replace

    return my_new_list
    # 2 autres solutions : compréhension
    # return [x if x != search else replace for x in my_list ]
    # return list(map(lambda x: x if x != search else replace, my_list))
