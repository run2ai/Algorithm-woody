# https://www.acmicpc.net/problem/13023

import sys


def dfs(node, depth):
    global graph, found
    visited[node] = True

    if depth == 5:
        found = True
        return

    for g in graph[node]:
        if not visited[g]:
            dfs(g, depth + 1)

    visited[node] = False


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    # 친구 관계 그래프 생성
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # 깊이가 5인 친구 관계가 존재하는지 확인
    found = False
    visited = [False] * n
    depth = 1
    for i in range(n):
        dfs(i, depth)
        if found:
            break

    print(1 if found else 0)
