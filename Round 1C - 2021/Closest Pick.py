
def get_1p_wins(lv, rv, k):
    if lv != 0 and rv != k + 1:
        return (rv - lv) // 2
    else:
        return rv - lv - 1


def get_2p_wins(lv, rv):
    return rv - lv - 1


def solve_case(case_id):
    n, k = map(int, input().split())
    p = [0] + sorted(map(int, input().split())) + [k + 1]
    ans = 0.
    probs_1p = sorted([get_1p_wins(l, r, k) for l, r in zip(p, p[1:])])
    probs_2p = [get_2p_wins(l, r) for l, r in zip(p, p[1:])]
    ans = max(ans, *probs_2p)
    ans = max(ans, sum(probs_1p[-2:]))
    print(f'Case #{case_id}: {ans / k:.9f}')


def main():
    t = int(input())
    for i in range(t):
        solve_case(i + 1)


if __name__ == '__main__':
    main()
