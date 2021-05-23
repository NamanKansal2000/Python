import math


def check(lst, flag, string):
    # if all char are same in string
    if flag == 1:
        return len(string)
    elif flag == 0:
        # since remaining list has all the dict elements with equal values
        # so we extract a value of first element
        mydict = lst[0]
        return mydict[list(mydict.keys())[0]]
    # if all char are diffrent or no pattern exists
    else:
        return 1


def max_lst(lst):
    max = 0
    for i in lst:
        # list(dict.values()) gives list all the values in dictionary
        m = sum(i.values())
        if m > max:
            max = m
    n_lst = []
    for i in lst:
        # we extract all the dictionary with max sum
        if sum(i.values()) == max:
            n_lst.append(i)

    return (n_lst)


def sub(string, k):
    counts = dict()
    # this will make all the possible substring of given length k
    parts = [string[i:i+k] for i in range(0, len(string), k)]
    # add it in dictionary to get count
    for part in parts:
        counts[part] = counts.get(part, 0)+1
    # if we have more than 1 element in dict then it means case is not possible
    # as similar M&M can't distributed.
    if len(counts) == 1:
        return counts
    else:
        return None


def possible(str, k):
    l = []
    for i in range(0, k):
        # i=0 is our original string
        if i == 0:
            l.append(str)
        else:
            # max k-1 letters shifted to the end of the string will form a new string
            # if k letters shifted then new sequence will have same substring as original string
            # only order will be shifted
            l.append(str[i:]+str[0:i])
    return l


def div(n):
    l = []
    for i in range(2, math.floor(n**0.5)+1):
        if n % i == 0:
            l.append(i)
    for i in reversed(l):
        l.append(int(n/i))
    return l


def same(s):
    n = len(s)
    # if all char equal to char[0]
    for i in range(1, n):
        if s[i] != s[0]:
            return 0

    return 1


def solution(string):
    # this checks if all the characters in string are same or not
    flag = same(string)
    # this will reduce time as then ans = len(string)
    if flag == 0:
        # calculates the no of possible slices
        k = div(len(string))
        lst = []
        for i in k:
            # possible gives all the possible string as its a circular list of char
            #l = possible(string, i)
            # now check for each substring how many parts can be made and save it in a dict
            # for str in l:
            k = sub(str, i)
            # if k != None:
            # store all dict with only one element
            lst.append(k)
        # this if statement for case when all char of string are diffrent then
        # our sub fxn will give None check if string = 'abcd'
        # counts={'ab':1,'cd':1} and this will return None then our ans is 1
        # means one complete slice to one minnion
        if lst == []:
            flag = 2
            check([], flag, string)
        # get the dict that has max sum of values in it since we need to maximize no of slices
        n_lst = max_lst(lst)
        # this will return desired output change print to return before submitting
        print(check(n_lst, flag, string))
    else:
        # if all the char are same in our string
        print(check([], flag, string))


string = 'bccbaabccbaa'
solution(string)
