from lab2.utils import open_file, write_file

def majority(a):
    dic = {}
    for i in a:
        dic[i] = dic.get(i, 0) + 1

    for l, m in dic.items():
        if m > len(a) // 2:
            return 1
    return 0



if __name__ == '__main__':
    n_str, m = open_file("../txtf/input.txt")
    n = int(n_str[0])
    ans = majority(m)
    write_file(ans, "../txtf/output.txt")

