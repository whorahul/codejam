def hungarian(a):
    if not a:
        return 0, []
    n, m = len(a)+1, len(a[0])+1
    u, v, p, ans = [0]*n, [0]*m, [0]*m, [0]*(n-1)
    for i in xrange(1, n):
        p[0] = i
        j0 = 0  # add "dummy" worker 0
        dist, pre = [float("inf")]*m, [-1]*m
        done = [False]*(m+1)
        while True:  # dijkstra
            done[j0] = True
            i0, j1, delta = p[j0], None, float("inf")
            for j in xrange(1, m):
                if done[j]:
                    continue
                cur = a[i0-1][j-1]-u[i0]-v[j]
                if cur < dist[j]:
                    dist[j], pre[j] = cur, j0
                if dist[j] < delta:
                    delta, j1 = dist[j], j
            for j in xrange(m):
                if done[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    dist[j] -= delta
            j0 = j1
            if not p[j0]:
                break
        while j0:  # update alternating path
            j1 = pre[j0]
            p[j0], j0 = p[j1], j1
    for j in xrange(1, m):
        if p[j]:
            ans[p[j]-1] = j-1
    return -v[0], ans  # min cost

def retiling():
    R, C, F, S = map(int, raw_input().strip().split())
    src, dst = [[raw_input().strip() for _ in xrange(R)] for _ in xrange(2)]
    pos0 = [(i, j) for i in xrange(R) for j in xrange(C) if src[i][j] == 'M']
    pos1 = [(i, j) for i in xrange(R) for j in xrange(C) if dst[i][j] == 'M']
    cost = [[0]*(len(pos0)+len(pos1)) for _ in xrange(len(pos0)+len(pos1))]
    for i in xrange(len(cost)):
        for j in xrange(len(cost[0])):
            if i < len(pos0) and j < len(pos1):
                cost[i][j] = S * (abs(pos0[i][0]-pos1[j][0])+abs(pos0[i][1]-pos1[j][1]))
            elif i < len(pos0) or j < len(pos1):
                cost[i][j] = F
    return hungarian(cost)[0]

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, retiling())
