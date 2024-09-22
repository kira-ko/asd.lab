with open("input.txt", "r") as f:
    a, b = map(int, f.readline().split())
f.close()

with open("output.txt", "w") as f:
    if (-10**9 <= a <= 10**9) and (-10**9 <= b <= 10**9):
        f.write(str(a + b ** 2))
    else:
        print('Числа не подходят по диапазону')
f.close()