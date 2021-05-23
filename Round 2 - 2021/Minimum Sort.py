def solve(n):
    for i in range(1, n):
        # find minimum in [i, n]
        print(f'M {i} {n}', flush=True)
        j = int(input())
        if i != j:
            print(f'S {i} {j}', flush=True)
            x = int(input())
            assert x == 1
    print('D', flush=True)
    x = int(input())
    assert x == 1


def main():
    t, n = map(int, input().split())
    for _ in range(t):
        solve(n)


if __name__ == '__main__':
    main()
