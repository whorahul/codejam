from math import gcd


class ImpossibleError(Exception):
    pass


def check(m, us, a, b):
    counts = [0 for _ in range(m + 1)]
    counts[m] = 1
    max_val = max(us) * len(us)
    for i in range(m, 0, -1):
        if i < len(us):
            if counts[i] < us[i]:
                return False
            x = counts[i] - us[i]
        else:
            x = counts[i]
        if i - a >= 0:
            counts[i - a] = min(counts[i - a] + x, max_val)
        if i - b >= 0:
            counts[i - b] = min(counts[i - b] + x, max_val)
    return True


def solve(n, us, a, b):
    assert n + 1 == len(us)
    needed = {i for i, u in enumerate(us) if u > 0}
    diffs = {i - min(needed) for i in needed}
    d = gcd(a, b)
    if not all(diff % d == 0 for diff in diffs):
        raise ImpossibleError()
    m = n
    while not check(m, us, a, b):
        m += 1
    return m


def main():
    for i in range(int(input())):
        n, a, b = map(int, input().split())
        us = [0] + [int(x) for x in input().split()]
        try:
            answer = solve(n, us, a, b)
        except ImpossibleError:
            answer = 'IMPOSSIBLE'
        print('Case #{}: {}'.format(i + 1, answer))


if __name__ == '__main__':
    main()
