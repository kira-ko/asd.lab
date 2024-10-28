def binary_search(array, whatfind):
    l = 0
    r = len(array) - 1

    while l <= r:
        middle = (l + r) // 2
        if array[middle] == whatfind:
            return middle
        elif array[middle] < whatfind:
            l = middle + 1
        else:
            r = middle - 1
    return -1

def func(mas, maas_find):
    return [binary_search(mas, maas_find[i]) for i in range(len(maas_find))]



if __name__ == '__main__':
    file = open('input.txt')
    n, mass = int(file.readline()), list(map(int, file.readline().split()))
    k, mass_f = int(file.readline()), list(map(int, file.readline().split()))

    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, func(mass, mass_f))))
