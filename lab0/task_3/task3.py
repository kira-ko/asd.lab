



def fib2():
    f = open("input.txt", "r")
    n = int(f.readline())
    f.close()
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, (a + b) % 10
        f = open("output.txt", "w")
        f.write(str(b))
        f.close()


fib2()
