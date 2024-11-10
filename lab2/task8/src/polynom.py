from lab2.utils import open_file, write_file

def multiplication_polynomials(a, b, n):
    result = [0] * (n + n - 1)
    for cof_a in range(n):
        for cof_b in range(n):
            result[cof_a + cof_b] += a[cof_b] * b[cof_a]
    return result


if __name__ == '__main__':
    a, b = open_file("../txtf/input.txt")
    n = a[0]
    a = a[1:]

    ans = multiplication_polynomials(a, b, n)
    write_file(ans, "../txtf/output.txt")
