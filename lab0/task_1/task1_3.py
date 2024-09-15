with open("input.txt", "r") as f:
    a, b = map(int, f.readline().split())
f.close()

with open("output.txt", "w") as f:
    f.write(str(a + b))
f.close()