# https://www.acmicpc.net/problem/2178

import sys
from collections import deque


def count_minimum_exit_traversal(n, m, maze):
    visited_maze = [[False for _ in range(m)] for _ in range(n)]

    # 이동 가능한 방향 좌표 설정
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 0,0에서 시작
    queue = deque([[0, 0]])

    while queue:
        now = queue.popleft()

        # 현재 위치에서 이동 가능한 다른 좌표를 큐에 삽입
        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]

            if x >= 0 and y >= 0 and x < n and y < m and visited_maze[x][y] == False and maze[x][y] != 0:
                # 현재 좌표 방문 완료 처리
                queue.append([x, y])
                visited_maze[x][y] = True
                maze[x][y] = maze[now[0]][now[1]] + 1

    return maze[n-1][m-1]


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
    answer = count_minimum_exit_traversal(N, M, maze)
    print(answer)
