with open("input.txt", "r") as f:
    n = int(f.readline())
f.close()

with open("output.txt", "w") as f:
    if n <= 1:
        f.write(str(n))
    else:
        a = [0, 1]
        for i in range(1, n):
            a.append((a[i-1] + a[i]))
        print(*a)
        f.write(str(a[n]))
