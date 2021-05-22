from itertools import permutations, product

class NoSolutionError(Exception):
    pass

R = 12 * 60**2 * 10**9
eleven_inv = None
for i in range(11):
    if (i * R + 1) % 11 == 0:
        eleven_inv = (i * R + 1) // 11
assert eleven_inv is not None
assert (eleven_inv * 11) % R == 1


def get_hands(h, m, s, n):
    x = 60**2 * 10**9 * h + 60 * 10**9 * m + 10**9 * s + n
    assert 0 <= x < R
    return x, 12 * x % R, 720 * x % R


def equal_shifted(xs, ys):
    return [(x - xs[0]) % R for x in xs] == [(y - ys[0]) % R for y in ys]    


def solve_rotated(a, b, c):
    for h, m in product(range(12), range(60)):
        H = 60**2 * 10**9 * h
        M = 60 * 10**9 * m
        N = eleven_inv * (H - 11*M - (a - b)) % R
        if 0 <= N < 60 * 10**9:
            s = N // 10**9
            n = N % 10**9
            if equal_shifted(get_hands(h, m, s, n), (a, b, c)):
                return h, m, s, n
    raise NoSolutionError()


def solve(a, b, c):
    for xs in permutations((a, b, c)):
        try:
            return solve_rotated(*xs)
        except NoSolutionError:
            pass
    assert False


def main():
    for i in range(int(input())):
        a, b, c = map(int, input().split())
        answer = solve(a, b, c)
        print('Case #{}: {}'.format(i + 1, ' '.join(map(str, answer))))


if __name__ == '__main__':
    main()
