import sys

def choose(a, b):
    c = 1
    for i in range(a, a - b, -1):
        c *= i
    for i in range(2, b + 1):
        c //= i
    return c

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

t = int(sys.stdin.readline())
for tt in range(1, t + 1):
    n, q = sys.stdin.readline().split()
    n, q = int(n), int(q)
    ans = [None] * n
    scores = [None] * n
    for i in range(n):
        ans[i], scores[i] = sys.stdin.readline().split()
        scores[i] = int(scores[i])
    if n == 1:
        if scores[0] * 2 >= q:
            a = ans[0]
            s = scores[0]
        else:
            a = "".join(["T" if c == "F" else "F" for c in ans[0]])
            s = q - scores[0]
        print(f"Case #{tt}: {a} {s}/1")
    elif n == 2:
        diffs = sum([1 if ans[0][i] != ans[1][i] else 0 for i in range(q)])
        sames = q - diffs
        sames_score = (scores[0] + scores[1] - diffs) // 2
        a = ""
        s = max(scores[0], scores[1]) - sames_score + (sames_score if sames_score * 2 >= sames else sames - sames_score)
        for i in range(q):
            if ans[0][i] == ans[1][i]:
                a += ans[0][i] if sames_score * 2 >= sames else ("T" if ans[0][i] == "F" else "F")
            else:
                a += ans[0][i] if scores[0] > scores[1] else ans[1][i]
        print(f"Case #{tt}: {a} {s}/1")
    else:
        at, bt, ct, dt = 0, 0, 0, 0
        for i in range(q):
            if ans[0][i] == ans[1][i] and ans[1][i] == ans[2][i]:
                at += 1
            elif ans[1][i] == ans[2][i]:
                bt += 1
            elif ans[0][i] == ans[2][i]:
                ct += 1
            elif ans[0][i] == ans[1][i]:
                dt += 1
        bdiff = -(scores[1] + scores[2] - ct - dt - 2 * bt) // 2
        cdiff = -(scores[0] + scores[2] - bt - dt - 2 * ct) // 2
        ddiff = -(scores[0] + scores[1] - bt - ct - 2 * dt) // 2
        denominator = 0
        aexp, bexp, cexp, dexp = 0, 0, 0, 0
        ainv, binv, cinv, dinv = False, False, False, False
        for ac in range(at + 1):
            bc = ac + bdiff
            cc = ac + cdiff
            dc = ac + ddiff
            if bc < 0 or bc > bt or cc < 0 or cc > ct or dc < 0 or dc > dt:
                continue
            ways = choose(at, ac) * choose(bt, bc) * choose(ct, cc) * choose(dt, dc)
            denominator += ways
            aexp += ac * ways
            bexp += bc * ways
            cexp += cc * ways
            dexp += dc * ways
        if aexp * 2 < denominator * at:
            ainv = True
            aexp = denominator * at - aexp
        if bexp * 2 < denominator * bt:
            binv = True
            bexp = denominator * bt - bexp
        if cexp * 2 < denominator * ct:
            cinv = True
            cexp = denominator * ct - cexp
        if dexp * 2 < denominator * dt:
            dinv = True
            dexp = denominator * dt - dexp
        numerator = aexp + bexp + cexp + dexp
        divisor = gcd(numerator, denominator)
        numerator //= divisor
        denominator //= divisor
        a = ""
        for i in range(q):
            if ans[0][i] == ans[1][i] and ans[1][i] == ans[2][i]:
                if ainv:
                    a += "T" if ans[0][i] == "F" else "F"
                else:
                    a += ans[0][i]
            elif ans[1][i] == ans[2][i]:
                a += ans[1][i] if binv else ans[0][i]
            elif ans[0][i] == ans[2][i]:
                a += ans[2][i] if cinv else ans[1][i]
            elif ans[0][i] == ans[1][i]:
                a += ans[0][i] if dinv else ans[2][i]

        print(f"Case #{tt}: {a} {numerator}/{denominator}")
