# https://www.acmicpc.net/problem/2751

import sys


def sort_in_ascending(numbers):
    return sorted(numbers)


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    numbers = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    answer = sort_in_ascending(numbers)
    print(*answer, sep='\n')
