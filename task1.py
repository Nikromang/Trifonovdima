import sys

N,M = [int(x) for x in input().split()]

def read_graph_as_matrix(n, m):
    graph = [[None]*n for i in range(n)]
    for j in range(1, m+1):
        a, b = map(int, input().split())
        graph[a][b] = b
    return graph

def call_all_friends(me,friends,already_called = None, stack = None):
    if already_called is None:
        already_called = set()
    if stack is None:
        stack = []
    already_called.add(me)
    stack.append(me)
    for friend in friends[me]:
        if friend == None:
            continue
        if friend not in already_called:
            call_all_friends(friend,friends,already_called,stack)
        elif friend == stack[0]:
            print(*stack)
            sys.exit()
    stack.pop(-1)

A = read_graph_as_matrix(N, M)
print(A)
for i in range(N):
    call_all_friends(i, A)
print('YES')







