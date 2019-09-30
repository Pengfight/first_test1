def swap(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp


def permutation(arr, cursor, k):
    if cursor == k:
        print(arr)
    for i in range(cursor, k + 1):
        swap(arr, cursor, i)
        # print(arr)
        permutation(arr, cursor + 1, k)
        swap(arr, cursor, i)
    '''if k != cursor:
        permutation(arr, cursor+1, k)'''


def factorial(n):
    if n <= 2:
        return 2
    else:
        print(n)
        return n * factorial(n - 1)


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    permutation(a, 0, len(a)-1)
    # print(factorial(4))
