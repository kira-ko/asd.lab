def majority(a):
    dic = {}
    for i in a:
        dic[i] = dic.get(i, 0) + 1

    for l, m in dic.items():
        if m > len(a) // 2:
            return 1
    return 0



if __name__ == '__main__':
    with open('../txtf/output.txt', 'w') as f:
        file = open('../txtf/input.txt')

        n = int(file.readline())
        list_input = list(map(int, file.readline().split()))

        f.write(str(majority(list_input)))