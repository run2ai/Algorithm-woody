# https://www.acmicpc.net/problem/1920

import sys

n = int(sys.stdin.readline().rstrip())
filter_number = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
checking_number = list(map(int, sys.stdin.readline().split()))

for check in checking_number:
    if check in filter_number:
        print(1)
    else:
        print(0)
