"""Задание 3. Сортировка вставкой по убыванию."""
def insertion_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, mas = f.readlines()
    array = insertion_descending(list(map(int, mas.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array))), file=f)