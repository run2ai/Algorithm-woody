
# https://www.acmicpc.net/problem/10989

import sys

if __name__ == '__main__':
    inp = sys.stdin.readline
    dic = dict()

    for _ in range(int(inp())):
        number = int(inp())
        try:
            dic[number] += 1  # 딕셔너리 key:숫자 value: 중복된 횟수
        except:
            dic[number] = 1

    dic = sorted(dic.items())
    for key, value in dic:
        for _ in range(value):
            print(key)
