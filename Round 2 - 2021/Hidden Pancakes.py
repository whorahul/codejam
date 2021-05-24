def nCr(n, k):
    while len(inv) <= n:  # lazy initialization
        fact.append(fact[-1]*len(inv) % MOD)
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
    return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

def hidden_pancakes():
    N = input()
    V = map(int, raw_input().strip().split())
    V.append(1)
    result = 1
    stk = []
    for v in V:
        if not (v <= len(stk)+1):
            return 0
        cnt = 0
        while v < len(stk)+1:
            result = result * nCr(cnt+(stk[-1]-1), (stk[-1]-1)) % MOD
            cnt += stk.pop()
        stk.append(cnt+1)
    return result

MOD = 10**9+7
fact = [1, 1]
inv = [0, 1]
inv_fact = [1, 1]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, hidden_pancakes())
