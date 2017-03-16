N,M = [int(x) for x in input().split()]
edges = []
for i in range(M):
    v1,v2,weight = list(map(int, input().split()))
    edges.append([weight, v1, v2])
edges.sort()
comp = [i for i in range(N)]
tree = []
tree_weight = 0
for weight, v1, v2 in edges:
    if comp[v1] != comp[v2]:
        tree_weight += weight
        tree.append((v1, v2))
        a = comp[v1]
        b = comp[v2]
        for i in range(N):
            if int(comp[i]) == b:
                comp[i] = a
tree.sort()
print(tree_weight)
for i in tree:
    print(*i)
