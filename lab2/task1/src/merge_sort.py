'''Сортировка слиянием'''
from lab2.utils import open_file, write_file


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

if __name__ == '__main__':
    n_str, m = open_file("../txtf/input.txt")
    n = int(n_str[0])
    ans = merge_sort(m)
    write_file(ans,"../txtf/output.txt" )



