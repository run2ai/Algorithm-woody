# https://www.acmicpc.net/problem/11004

import sys


def get_kth_number(numbers, k):
    return sorted(numbers)[k-1]


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    answer = get_kth_number(numbers, k)
    print(answer)
