import sys

t = int(sys.stdin.readline())
for tt in range(1, t + 1):
    m = int(sys.stdin.readline())
    p = [None] * m
    n = [None] * m
    total = 0
    for i in range(m):
        p[i], n[i] = sys.stdin.readline().split()
        p[i], n[i] = int(p[i]), int(n[i])
        total += p[i] * n[i]
    ans = 0
    for num in range(total, max(2, total - 4000), -1):
        num2 = num
        cursum = 0
        for i in range(m):
            for j in range(n[i]):
                if num2 % p[i] != 0:
                    break
                num2 //= p[i]
                cursum += p[i]
            if num2 == 1:
                break
        if num2 == 1 and cursum + num == total:
            ans = num
            break
    print(f"Case #{tt}: {ans}")
