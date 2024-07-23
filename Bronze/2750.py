
# https://www.acmicpc.net/problem/2750

import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    numbers = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    answer = sorted(numbers)
    print(*answer, sep=' ')
