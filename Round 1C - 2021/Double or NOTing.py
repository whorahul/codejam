INF = 2 ** 31


def inverse(s):
    return ''.join('0' if c == '1' else '1' for c in s).lstrip('0')


def get_patterns(s):
    res = []
    cnt = 1
    while s != '':
        res.append((s, cnt))
        cnt += 1
        s = inverse(s)
    res.append((s, cnt))
    return res


def count_n_grps(s):
    if len(s) == 0:
        return 0
    return 1 + sum(x != y for x, y in zip(s, s[1:]))


def match_pat(s, n_grps):
    need_n_grps = count_n_grps(s)
    return (
        need_n_grps < n_grps
        or need_n_grps == n_grps and s[-1] == '0'
    )


def solve_case(case_id):
    s, e = input().split()
    ans = INF
    add = 0
    if s == '0':
        if e == '0':
            ans = 0
        else:
            s = '1'
            add = 1
    patterns = get_patterns(s)
    for pat, n_grps in patterns:
        if e.startswith(pat) and match_pat(e[len(pat):], n_grps):
            cost = n_grps - 1 + len(e) - len(pat)
            ans = min(ans, cost)
    if e == '0':
        ans = min(ans, len(patterns) - 1)
    if ans == INF:
        print(f'Case #{case_id}: IMPOSSIBLE')
    else:
        print(f'Case #{case_id}: {ans + add}')


def main():
    t = int(input())
    for case_id in range(1, t + 1):
        solve_case(case_id)


if __name__ == '__main__':
    main()
