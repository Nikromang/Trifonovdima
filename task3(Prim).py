N,M = [int(x) for x in input().split()]
edges = []
for i in range(M):
    v1,v2,weight = list(map(int, input().split()))
    edges.append([weight,v1,v2])
edges.sort()
comp = list(range(N))
tree = []
tree_weight = 0
for weight,v1,v2 in edges:
    if comp[v1]!=comp[v2]:
        tree.append((v1,v2))
        for i in range(N):
            if comp[i] == comp[v2]:
                comp[i] = comp[v1]

tree.sort()
print(tree_weight)
for i in range

n, m = map(int, input().split())
edge = []
for i in range(m):
    s, e, w = map(int, input().split())
    edge.append([w, s, e])
edge.sort()
comp = [i for i in range(n)]
Ans = 0
Q = []
for w, s, e in edge:
    if comp[s] != comp[e]:
        Ans += w
        Q.append([s, e])
        a = comp[s]
        b = comp[e]
        for i in range(n):
            if comp[i] == b:
                comp[i] = a
Q.sort()
print(Ans)
for i in Q:
    print(*i)
