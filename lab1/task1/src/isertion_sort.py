def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, massive = f.readlines()
    array = insertion_sort(list(map(int, massive.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array))), file=f)