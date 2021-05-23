# This function use loop for removing duplicate
def loop(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)

    return new_lst


# This function use set() to remove duplicates
def use_set(lst):
    return set(lst)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
