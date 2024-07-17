# https://www.acmicpc.net/problem/2164

import sys
from collections import deque


def get_last_card_number(n):
    numbers = deque([x for x in range(1, n+1)])
    while len(numbers) != 1:
        numbers.popleft()
        numbers.append(numbers.popleft())

    return numbers[0]


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    answer = get_last_card_number(n)
    print(answer)
