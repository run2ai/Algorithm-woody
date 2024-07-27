# https://www.acmicpc.net/problem/11399

import sys


def calculate_min_time(times):
    result = 0

    sorted_times = sorted(times)
    for i, v in enumerate(sorted_times):
        result += sum(sorted_times[:i+1])

    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    times = list(map(int, sys.stdin.readline().split()))
    answer = calculate_min_time(times)
    print(answer)
