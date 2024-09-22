a, b = map(int, input().split())
f = True
while f:
    if (-10 ** 9 <= a <= 10 ** 9) and (-10 ** 9 <= b <= 10 ** 9):
        print(a + b**2)
        break
    else:
        print('Числа не подходят по диапазону')
        a, b = map(int, input().split())