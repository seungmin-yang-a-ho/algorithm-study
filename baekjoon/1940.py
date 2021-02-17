# https://www.acmicpc.net/problem/1940
# timeover
import sys
import itertools
input = sys.stdin.readline

N = int(input())
M = int(input())
L = list(map(int,input().split()))

all_pair = itertools.combinations(L,2)


result_cnt = 0
for pair in all_pair:
    cmp_result = sum(pair)
    if M == cmp_result:
        result_cnt = result_cnt + 1

print(result_cnt)

##------------------------------
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
L = sorted(list(map(int,input().split())))

result_cnt = 0
for idx, value in enumerate(L):
    if value >= M:
        break
    if idx+1 > len(L)-1:
        break
    for plus_item in L[idx+1:]:
        pair_sum = value + plus_item
        if pair_sum == M:
            result_cnt = result_cnt + 1
            continue
        if pair_sum > M:
            break

print(result_cnt)