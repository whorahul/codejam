import bisect


MAX_LEN = 19


def gen():
    r_years = set()
    # (I): All years from three or more consecutive numbers
    for v in range(1, 10 ** 6):
        cur_s = str(v) + str(v + 1) + str(v + 2)
        v += 2
        while len(cur_s) <= MAX_LEN:
            r_years.add(int(cur_s))
            v += 1
            cur_s += str(v)
    # (II): All years from two consevutive numbers of kind [(10 ** k) - 1; 10 ** k]
    for k in range(1, 10):
        v = 10 ** k - 1
        r_years.add(int(str(v) + str(v + 1)))
    return tuple(sorted(r_years))


def solve_case(case_id, r_years):
    str_y = input()
    int_y = int(str_y)
    # Find from cached variants of type (I) and (II)
    idx = bisect.bisect_right(r_years, int_y)
    ans = r_years[idx]
    # (III) Year as two consecutive numbers with equal length
    if len(str_y) % 2 == 0:
        k = len(str_y) // 2
        max_v = 10 ** k - 2
        prefix_y = int(str_y[:k])
        suffix_y = int(str_y[k:])
        if (prefix_y, suffix_y) < (max_v, max_v + 1):
            if suffix_y <= prefix_y:
                try_s = str(prefix_y) + str(prefix_y + 1)
            else:
                try_s = str(prefix_y + 1) + str(prefix_y + 2)
            ans = min(ans, int(try_s))
        else:
            # Uh, no such number
            pass
    else:
        # Find minimal number of type (III) with len + 1
        k = len(str_y) // 2 + 1
        min_v = 10 ** (k - 1)
        try_s = str(min_v) + str(min_v + 1)
        ans = min(ans, int(try_s))
    print(f'Case #{case_id}: {ans}')


def main():
    r_years = gen()
    t = int(input())
    for case_id in range(1, t + 1):
        solve_case(case_id, r_years)


if __name__ == '__main__':
    main()
