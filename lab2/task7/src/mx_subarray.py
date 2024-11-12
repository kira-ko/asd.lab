'''Поиск максимального подмассива'''
from lab2.utils import open_file, write_file


def max_subarray(array):
    mx_summ = 0
    summ = 0
    for i in range(len(array)):
        if summ == 0:
            start = i
        summ += array[i]
        if mx_summ < summ:
            mx_summ = summ
            finish = i
        if summ < 0:
            summ = 0
    return array[start:finish + 1]

if __name__ == '__main__':
    n_str, m = open_file("../txtf/input.txt")
    n = int(n_str[0])

    ans = max_subarray(m)
    write_file(ans, "../txtf/output.txt")