import operator
import math


def arr_traversing(arr):
    for i in arr:
        print(i, end=' ')
    print()


def dictionary_sort(arr, k):
    """
    eg: arr = [8,3,9,6,4,7,5,2,1]
    """
    # covert to the number of mediators
    temp_arr = list(range(len(arr)))
    for i in range(len(arr)):
        flag = 0
        for j in range(i, len(arr), 1):
            if arr[j] < arr[i]:
                flag += 1
        # print(arr[i])
        # print(arr[i] - flag)
        temp_arr[i] = flag
    temp_arr.reverse()
    print(temp_arr)
    # the addition of increase_method
    if k >= 0:
        add_num = k
        for i in range(1, len(temp_arr)):
            '''if temp_arr[len(temp_arr) - 1] == 0 or operator.eq([i for i in range(len(arr))], temp_arr):
                #print('1')
                arr_traversing([i for i in range(len(arr), 0, -1)])
                return'''
            # decimal = decimal
            if add_num == 0:
                break
            temp_add = add_num
            add_num = (temp_arr[i] + add_num) // (math.factorial(i))
            temp_arr[i] = (temp_arr[i] + temp_add) % (math.factorial(i))
        # print(temp_arr)
        # reverse the arr
        # print(temp_arr)
        '''if temp_arr[len(temp_arr) - 1] == 0:
            # print('1')
            arr_traversing([i for i in range(len(arr), 0, -1)])
            return'''
    else:
        sub_num = -k
        for i in range(len(temp_arr)):
            '''if temp_arr[len(temp_arr) - 1] == 0 or operator.eq([i for i in range(len(arr))], temp_arr):
                #print('1')
                arr_traversing([i for i in range(len(arr), 0, -1)])
                return'''
            # decimal = decimal
            if sub_num == 0:
                break
            temp_num = sub_num
            sub_num = temp_num // (math.factorial(i))
            if (temp_arr[i] - temp_num % (math.factorial(i))) < 0:
                temp_arr[i] = temp_arr[i] + (math.factorial(i)) * 1 - (temp_num % (math.factorial(i)))
                for j in range(i + 1, len(temp_arr)):
                    if temp_arr[j] - 1 < 0:
                        temp_arr[j] = math.factorial(j) + 1 - 1
                        temp_arr[j + 1] = temp_arr[j + 1] - 1
            else:
                temp_arr[i] = temp_arr[i] - (temp_num % math.factorial(i))

            '''temp_arr[i] = (temp_arr[i]) % (i + 1)
            sub_num = (temp_arr[i]) // (i + 1)'''

    temp_arr.reverse()
    # print(temp_arr)

    # covert to original permutation
    original_arr = list(range(len(arr)))
    sub_arr = []
    # print(sub_arr)
    for i in range(len(original_arr)):
        permutation_num = len(original_arr) - i
        flag_sub = temp_arr[i]
        for sub in sub_arr:
            if flag_sub >= sub:
                flag_sub += 1
            else:
                break
        sub_arr.append(flag_sub)
        sub_arr.sort()
        original_arr[flag_sub] = permutation_num
    original_arr.reverse()
    arr_traversing(original_arr)
    # print(original_arr)


def increase_method(arr, k):
    # covert to the number of mediators
    temp_arr = list(range(len(arr)))
    for i in range(len(arr)):
        flag = 0
        for j in range(i, len(arr), 1):
            if arr[j] < arr[i]:
                flag += 1
        # print(arr[i])
        # print(arr[i] - flag)
        temp_arr[arr[i] - 1] = flag
    # print(temp_arr)
    '''if operator.eq([i for i in range(len(arr))], temp_arr):
        arr_traversing(arr)
        return'''
    # the addition of increase_method
    # print(sorted(temp_arr))
    # temp_arr = [8, 7, 6, 5, 4, 3, 2, 0, 0]
    # temp_arr.reverse()
    if k >= 0:
        add_num = k
        for i in range(len(temp_arr)):
            '''if temp_arr[len(temp_arr) - 1] == 0 or operator.eq([i for i in range(len(arr))], temp_arr):
                #print('1')
                arr_traversing([i for i in range(len(arr), 0, -1)])
                return'''
            # decimal = decimal
            if add_num == 0:
                break
            temp_add = add_num
            add_num = (temp_arr[i] + add_num) // (i + 1)
            temp_arr[i] = (temp_arr[i] + temp_add) % (i + 1)
        # print(temp_arr)
        # reverse the arr
        # print(temp_arr)
        '''if temp_arr[len(temp_arr) - 1] == 0:
            # print('1')
            arr_traversing([i for i in range(len(arr), 0, -1)])
            return'''
    else:
        sub_num = -k
        for i in range(len(temp_arr)):
            '''if temp_arr[len(temp_arr) - 1] == 0 or operator.eq([i for i in range(len(arr))], temp_arr):
                #print('1')
                arr_traversing([i for i in range(len(arr), 0, -1)])
                return'''
            # decimal = decimal
            if sub_num == 0:
                break
            temp_num = sub_num
            sub_num = temp_num // (i + 1)
            if (temp_arr[i] - temp_num % (i + 1)) < 0:
                temp_arr[i] = temp_arr[i] + (i + 1) * 1 - (temp_num % (i + 1))
                for j in range(i + 1, len(temp_arr)):
                    if temp_arr[j] - 1 < 0:
                        temp_arr[j] = j + 1 - 1
                        temp_arr[j + 1] = temp_arr[j + 1] - 1
            else:
                temp_arr[i] = temp_arr[i] - (temp_num % (i + 1))

            '''temp_arr[i] = (temp_arr[i]) % (i + 1)
            sub_num = (temp_arr[i]) // (i + 1)'''

    temp_arr.reverse()
    # print(temp_arr)

    # covert to original permutation
    original_arr = list(range(len(arr)))
    sub_arr = []
    # print(sub_arr)
    for i in range(len(original_arr)):
        permutation_num = len(original_arr) - i
        flag_sub = temp_arr[i]
        for sub in sub_arr:
            if flag_sub >= sub:
                flag_sub += 1
            else:
                break
        sub_arr.append(flag_sub)
        sub_arr.sort()
        original_arr[flag_sub] = permutation_num
    original_arr.reverse()
    arr_traversing(original_arr)
    # print(original_arr)


def decrease_method(arr, k):
    # covert to the number of mediators
    """temp_arr = list(range(len(arr)))
    for i in range(len(arr)):
        flag = 1
        for j in range(i):
            if arr[j] < arr[i]:
                flag += 1
        # print(arr[i])
        # print(arr[i] - flag)
        temp_arr[arr[i] - 1] = arr[i] - flag"""
    temp_arr = list(range(len(arr)))
    for i in range(len(arr)):
        flag = 0
        for j in range(i, len(arr), 1):
            if arr[j] < arr[i]:
                flag += 1
        # print(arr[i])
        # print(arr[i] - flag)
        temp_arr[arr[i] - 1] = flag
    # print(temp_arr)
    # reverse the arr to decrease_method
    temp_arr.reverse()

    # the addition of increase_method
    if k >= 0:
        add_num = k
        for i in range(len(temp_arr)):
            if add_num == 0:
                break
            temp_add = add_num
            add_num = (temp_arr[i] + add_num) // (len(temp_arr) - i)
            temp_arr[i] = (temp_arr[i] + temp_add) % (len(temp_arr) - i)
        # print(temp_arr)
        # reverse the arr
        # temp_arr.reverse()
        # print(temp_arr)
    else:
        sub_num = -k
        for i in range(len(temp_arr)):
            '''if temp_arr[len(temp_arr) - 1] == 0 or operator.eq([i for i in range(len(arr))], temp_arr):
                #print('1')
                arr_traversing([i for i in range(len(arr), 0, -1)])
                return'''
            # decimal = decimal
            if sub_num == 0:
                break
            temp_num = sub_num
            sub_num = temp_num // (len(temp_arr) - i)
            if (temp_arr[i] - temp_num % (len(temp_arr) - i)) < 0:
                temp_arr[i] = temp_arr[i] + (len(temp_arr) - i) * 1 - (temp_num % (len(temp_arr) - i))
                for j in range(i + 1, len(temp_arr)):
                    if temp_arr[j] - 1 < 0:
                        temp_arr[j] = j + 1 - 1
                        temp_arr[j + 1] = temp_arr[j + 1] - 1
            else:
                temp_arr[i] = temp_arr[i] - (temp_num % (len(temp_arr) - i))

        # print(temp_arr)

    # covert to original permutation
    original_arr = list(range(len(arr)))
    sub_arr = []
    for i in range(len(original_arr)):
        permutation_num = len(original_arr) - i
        flag_sub = temp_arr[i]
        for sub in sub_arr:
            if flag_sub >= sub:
                flag_sub += 1
        sub_arr.append(flag_sub)
        sub_arr.sort()
        original_arr[flag_sub] = permutation_num
    original_arr.reverse()
    arr_traversing(original_arr)
    # print(original_arr)


if __name__ == '__main__':
    str1_in = input()
    n, type_method, k = [int(i) for i in str1_in.split()]
    str2_in = input()
    num = [int(i) for i in str2_in.split()]
    if type_method == 1:
        dictionary_sort(num, k)
    elif type_method == 2:
        increase_method(num, k)
    elif type_method == 3:
        decrease_method(num, k)
    else:
        decrease_method(num, k)
    '''my_arr = [8, 3, 9, 6, 4, 7, 5, 2, 1]
    my_arr1 = [3, 6, 4, 7, 5, 2, 1]
    # dictionary_sort(my_arr, 5)
    # increase_method(my_arr, 1)
    decrease_method(my_arr, 0)'''
    '''my_arr = [8, 3, 9, 6, 5, 1, 2, 4, 7]
    my_arr2 = [9, 8, 7, 6, 5, 4, 1, 3, 2]
    my_arr1 = [3, 6, 4, 7, 5, 2, 1]
    # for k in range(10):
    # dictionary_sort(my_arr, 10000000)
    for i in range(100000):
        increase_method(my_arr, i)'''
    '''my_arr2 = [9, 8, 7, 6, 5, 4, 1, 3, 2]
    # my_arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    my_arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    my_arr5 = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 3, 1, 2, 4]
    my_arr3 = [1, 2, 3, 4, 5]
    # for i in range(20):'''
    '''increase_method(my_arr5, 5)
    increase_method(my_arr5, 6)
    increase_method(my_arr5, 7)
    increase_method(my_arr5, 8)
    increase_method(my_arr5, 9)
    increase_method(my_arr5, 10)'''
    # my_arr4 = [i for i in range(1, 0, -1)]
    '''for k in range(1, 21):
        my_arr4 = [i for i in range(k, 0, -1)]
        # increase_method(my_arr4, -10000)
        increase_method(my_arr4, -math.factorial(k) + 1)'''



