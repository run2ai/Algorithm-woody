# https://www.acmicpc.net/problem/17298

import sys


def get_nge(numbers):
    stack = []
    result = [-1] * len(numbers)

    for i, v in enumerate(numbers[::-1]):  # 오른쪽에서 왼쪽으로 역방향 탐색
        while stack and stack[-1] <= v:
            stack.pop()

        if stack:
            result[i] = stack[-1]
        stack.append(v)

    return result[::-1]


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    sequence = list(map(int, sys.stdin.readline().split()))
    answer = get_nge(sequence)
    print(*answer, sep=' ')
