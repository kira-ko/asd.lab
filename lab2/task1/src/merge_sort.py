'''Сортировка слиянием'''
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
    with open('output.txt', 'w') as f:
        file = open('input.txt')
        n = int(file.readline())
        array = list(map(int, file.readline().split()))

        f.write(' '.join(map(str, merge_sort(array))))