"""Задание 2. Сортировка вставкой +"""
def insertion_sort(list_arr):
    index_result = [1]
    for i in range(1, len(list_arr)):
        for j in range(i - 1, -1, -1):
            if list_arr[i] < list_arr[j]:
                list_arr[i], list_arr[j] = list_arr[j], list_arr[i]
                i, j = j, i
        index_result.append(i + 1)
    return index_result, list_arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, mas = f.readlines()
    ind, array = insertion_sort(list(map(int, mas.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, ind))), file=f)
        print(' '.join(list(map(str, array))), file=f)