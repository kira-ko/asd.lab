with open("input.txt", 'r') as f:
    n = int(f.readline())
f.close()

with open("output.txt", "w") as f:
    if n <= 1:
        f.write(str(n))
    else:
        a, b = 0, 1
        s = 0
        for i in range(1, n):
            s = (a+b)%10
            a, b = b, s
        f.write(str(s))
f.close()
