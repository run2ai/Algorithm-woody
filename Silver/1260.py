# https://www.acmicpc.net/problem/1260

import sys
from collections import deque


def dfs(graph, start):
    global dfs_result
    dfs_result.append(start)  # 탐색 시작 노드 저장

    for g in graph[start]:
        if g not in dfs_result:
            dfs(graph, g)

    return


def bfs(graph, start):
    global bfs_result
    bfs_result.append(start)  # 탐색 시작 노드 저장
    queue = deque(graph[start])
    while queue:
        popped = queue.popleft()
        bfs_result.append(popped)

        for e in graph[popped]:  # pop한 노드와 연결된 다른 노드를 큐에 저장
            if e not in queue and e not in bfs_result:
                queue.append(e)

    return


if __name__ == '__main__':
    # n: 노드 개수, m: 간선 개수, k: 탐색 시작 노드 번호
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]  # 양방향 연결 그래프 생성
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    # value 값을 오름차순으로 정렬
    for i in range(n+1):
        graph[i].sort()

    dfs_result, bfs_result = [], []

    dfs(graph, k)
    bfs(graph, k)

    print(*dfs_result, sep=' ')
    print(*bfs_result, sep=' ')
