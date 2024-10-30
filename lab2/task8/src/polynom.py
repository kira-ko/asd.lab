def multiplication_polynomials(a, b, n):
    result = [0] * (n + n - 1)
    for cof_a in range(n):
        for cof_b in range(n):
            result[cof_a + cof_b] += a[cof_b] * b[cof_a]
    return result


if __name__ == '__main__':
    with open('output.txt', 'w') as f:
        file = open('input.txt')
        n = int(file.readline())
        a, b = list(map(int, file.readline().split())), list(map(int, file.readline().split()))
        f.write(' '.join(map(str, multiplication_polynomials(a, b, n))))

