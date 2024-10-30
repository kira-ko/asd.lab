'''Задание 6. Пузырьковая сортировка.'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, mas = f.readlines()
    array = bubble_sort(list(map(int, mas.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array))), file=f)