# https://www.acmicpc.net/problem/11286

import sys
import heapq


def get_absolute_heap(numbers):
    heap = []

    for number in numbers:
        if number != 0:
            heapq.heappush(heap, (abs(number), number))  # 힙에 절댓값과 원래값을 추가
        else:
            if not heap:  # 힙이 비어있는 경우
                print(0)
            else:
                # 힙에서 절댓값이 가장 작은 값을 제거, 동일한 값이 존재한다면 원래값을 기준으로 제거
                print(heapq.heappop(heap)[1])


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    get_absolute_heap(numbers)
