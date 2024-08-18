# https://www.acmicpc.net/problem/11047

import sys


def get_minimum_coins(coins, money):
    result = 0

    while money != 0:
        for coin in coins[::-1]:
            if money >= coin:
                result += (money // coin)
                money = (money % coin)
                break

    return result


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    answer = get_minimum_coins(coins, k)
    print(answer)
