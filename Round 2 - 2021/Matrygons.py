def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i != n // i:
                ds.append(n // i)
        i += 1
    return ds

mem = {0: 0, 1: -1000}

def g(n):
    if n in mem:
        return mem[n]
    best = 1
    for p in divisors(n):
        if p > 1:
            best = max(best, g(n // p - 1) + 1)
    mem[n] = best
    return mem[n]

def f(n):
    best = 1
    for p in divisors(n):
        if p > 2:
            best = max(best, g(n//p - 1) + 1)
    return best

def solve():
    n = int(input())
    print(f(n))


def main():
    t = int(input())
    for test_case_num in range(1, t + 1):
        print(f'Case #{test_case_num}: ', end='')
        solve()
    pass


if __name__ == '__main__':
    main()
