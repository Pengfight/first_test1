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
    # print(temp_arr)
    # print(temp_arr)
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
            add_num = (temp_arr[i] + add_num) // (i + 1)
            temp_arr[i] = (temp_arr[i] + temp_add) % (i + 1)
            # print(add_num)
        # print(temp_arr)
        # reverse the arr
        # print(temp_arr)
        '''if temp_arr[len(temp_arr) - 1] == 0:
            # print('1')
            arr_traversing([i for i in range(len(arr), 0, -1)])
            return'''
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
            sub_num = temp_num // (i + 1)
            if (temp_arr[i] - (temp_num % (i + 1))) < 0:
                temp_arr[i] = temp_arr[i] + (i + 1) - (temp_num % (i + 1))
                temp_arr[i + 1] = temp_arr[i + 1] - 1
                if (i + 1) < len(temp_arr):
                    for j in range(i + 1, len(temp_arr)):
                        if temp_arr[j] < 0:
                            temp_arr[j] = (j + 1) + temp_arr[j]
                            if (j + 1) < len(temp_arr):
                                temp_arr[j + 1] = temp_arr[j + 1] - 1
            else:
                temp_arr[i] = temp_arr[i] - (temp_num % (i + 1))

            '''temp_arr[i] = (temp_arr[i]) % (i + 1)
            sub_num = (temp_arr[i]) // (i + 1)'''
        # print(temp_arr)
    temp_arr.reverse()
    # print(temp_arr)
    # covert to original permutation
    # original_arr = list(range(len(arr)))
    is_in_arr = []
    # print(sub_arr)
    for i in range(len(arr)):
        permutation_num = temp_arr[i] + 1
        # flag_sub = temp_arr[i]
        for sub in range(len(is_in_arr)):
            if permutation_num >= is_in_arr[sub]:
                permutation_num += 1
                # print(permutation_num, end=' ')
        is_in_arr.append(permutation_num)
        is_in_arr.sort()
        # print(is_in_arr)
        arr[i] = permutation_num

    # temp_arr.reverse()
    # print(arr)

    arr_traversing(arr)
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
            if (temp_arr[i] - (temp_num % (i + 1))) < 0:
                temp_arr[i] = temp_arr[i] + (i + 1) - (temp_num % (i + 1))
                temp_arr[i + 1] = temp_arr[i + 1] - 1
                if (i + 1) < len(temp_arr):
                    for j in range(i + 1, len(temp_arr)):
                        if temp_arr[j] < 0:
                            temp_arr[j] = temp_arr[j] + (j + 1)
                            if (j + 1) < len(temp_arr):
                                temp_arr[j + 1] = temp_arr[j + 1] - 1
            else:
                temp_arr[i] = temp_arr[i] - (temp_num % (i + 1))

            '''temp_arr[i] = (temp_arr[i]) % (i + 1)
            sub_num = (temp_arr[i]) // (i + 1)'''
        # print(temp_arr)

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
        '''sub_num = -k
        for i in range(len(temp_arr)):
            # decimal = decimal
            if sub_num == 0:
                break
            temp_num = sub_num
            sub_num = temp_num // (len(temp_arr) - i)
            if (temp_arr[i] - (temp_num % (len(temp_arr) - i))) < 0:
                temp_arr[i] = temp_arr[i] + (len(temp_arr) - i) * 1 - (temp_num % (len(temp_arr) - i))
                if (i + 1) < len(temp_arr):
                    for j in range(i + 1, len(temp_arr)):
                        if temp_arr[j] - 1 < 0:
                            temp_arr[j] = j + 1 - 1
                            if (j + 1) < len(temp_arr):
                                temp_arr[j + 1] = temp_arr[j + 1] - 1
            else:
                temp_arr[i] = temp_arr[i] - (temp_num % (len(temp_arr) - i))'''
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
            if (temp_arr[i] - (temp_num % (len(temp_arr) - i))) < 0:
                temp_arr[i] = temp_arr[i] + (len(temp_arr) - i) * 1 - (temp_num % (len(temp_arr) - i))
                temp_arr[i + 1] = temp_arr[i + 1] - 1
                if (i + 1) < len(temp_arr):
                    for j in range(i + 1, len(temp_arr)):
                        if temp_arr[j] < 0:
                            # temp_arr[j] = temp_arr[j] + j + 1
                            temp_arr[j] = temp_arr[j] + (len(temp_arr) - j)
                            if (j + 1) < len(temp_arr):
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
        # print(original_arr)
        original_arr[flag_sub] = permutation_num
    original_arr.reverse()
    arr_traversing(original_arr)
    # print(original_arr)


def adjacent_exchange_method(arr, k):
    # convert to the number of mediators
    # start at 2
    mediator_list = [0]
    # print(mediator_list)
    arrow_list = []
    sub = 1
    for i in range(2, len(arr)+1, 1):
        pos = arr.index(i)
        mediator_num = 0
        # i is odd? even number? to get direction of i
        if (i % 2) != 0:
            direction = mediator_list[sub-1] % 2
        else:
            direction = (mediator_list[sub-1] + mediator_list[sub-2]) % 2
        # get direction then calculating mediator_num
        if direction == 0 or i == 2:
            # from pos to right
            for j in range(pos + 1, len(arr)):
                if arr[j] < i:
                    mediator_num += 1
            mediator_list.append(mediator_num)
        else:
            # from pos to left
            for j in range(0, pos):
                if arr[j] < i:
                    mediator_num += 1
            mediator_list.append(mediator_num)
        sub += 1
    print(mediator_list)
    mediator_list.reverse()

    # the addition of mediator
    if k >= 0:
        add_num = k
        for i in range(len(mediator_list)):
            if add_num == 0:
                break
            temp_add = add_num
            add_num = (mediator_list[i] + add_num) // (len(mediator_list) - i)
            mediator_list[i] = (mediator_list[i] + temp_add) % (len(mediator_list) - i)
        # print(mediator_list)
        # reverse the arr
        # mediator_list.reverse()
        # print(mediator_list)
    # the subtraction of mediator
    else:
        sub_num = -k
        for i in range(len(mediator_list)):
            # decimal = decimal
            if sub_num == 0:
                break
            temp_num = sub_num
            sub_num = temp_num // (len(mediator_list) - i)
            if (mediator_list[i] - (temp_num % (len(mediator_list) - i))) < 0:
                mediator_list[i] = mediator_list[i] + (len(mediator_list) - i) * 1 - (temp_num % (len(mediator_list) - i))
                mediator_list[i + 1] = mediator_list[i + 1] - 1
                if (i + 1) < len(mediator_list):
                    for j in range(i + 1, len(mediator_list)):
                        if mediator_list[j] < 0:
                            # mediator_list[j] = mediator_list[j] + j + 1
                            mediator_list[j] = mediator_list[j] + (len(mediator_list) - j)
                            if (j + 1) < len(mediator_list):
                                mediator_list[j + 1] = mediator_list[j + 1] - 1
            else:
                mediator_list[i] = mediator_list[i] - (temp_num % (len(mediator_list) - i))

        # print(mediator_list)



if __name__ == '__main__':
    '''str1_in = input()
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
        decrease_method(num, k)'''
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
    # x1 = [7,  8,  4, 14, 12,  2, 17,  5, 10, 16, 13,  6, 11, 15,  1,  9,  3, 18]
    x1 = [i for i in range(19, 0, -1)]
    my_arr = [8, 3, 9, 6, 4, 7, 5, 2, 1]
    # increase_method(x1, -2)
    # decrease_method(x1, -2)
    # dictionary_sort(x1, -2)
    # decrease_method(x1, -math.factorial(19) + 2)
    adjacent_exchange_method(my_arr, -2)
    '''for num in range(5000):
        for i in range(10, 22):
            x = np.random.choice([j for j in range(1, i)], i-1, replace=False)
            print(x)
            increase_method(x, -math.factorial(8))
        print(num)'''

    # my_arr4 = [i for i in range(, 0, -1)]
    '''my_arr4 = [i for i in range(20, 0, -1)]
    for i in range(-math.factorial(10)+1, -math.factorial(1)+2):
        print(i, end=' ')
        increase_method(my_arr4, i)'''
