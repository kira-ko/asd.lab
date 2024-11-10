'''Бинарный поиск'''
from lab2.utils import open_file, write_file

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



if __name__ == '__main__':

    data_n, data_k = open_file("../txtf/input.txt")
    n = int(data_n[0])
    mass = data_n[1:]

    k = int(data_k[0])
    mass_f = data_k[1:]

    write_file("", "../txtf/output.txt", mode="w")
    for i in mass_f:
        ans = binary_search(mass, i)
        write_file(f"{ans} ", "../txtf/output.txt", mode='a')


