# https://www.acmicpc.net/problem/11274

import sys


def dfs(node, graph):
    global visited
    visited.add(node)  # 현재 노드 탐색 완료

    # 현재 노드에서 탐색 가능한 다른 노드 탐색
    for g in graph[node]:
        if g not in visited:
            dfs(g, graph)

    return


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    visited = set()
    graph = [[] for _ in range(n+1)]  # 양방향 그래프 생성
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    answer = 0
    for i in range(1, n+1):
        if i not in visited:
            dfs(i, graph)
            answer += 1

    print(answer)
