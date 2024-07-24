# https://www.acmicpc.net/problem/1427

import sys


def sort_descending_digit(n):
    str_number = sorted(str(n), reverse=True)  # 문자열로 바꿔서 내림차순 정렬
    return ''.join(str_number)


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    answer = sort_descending_digit(n)
    print(answer)
