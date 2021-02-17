#https://www.acmicpc.net/problem/1655
#time over
import sys
input = sys.stdin.readline

N = int(input())
integer_list = list()
for i in range(N):
    integer_list.append(int(input()))

result = list()
len_integer_list = len(integer_list)
for i in range(N):
    if i+1 > len_integer_list:
        break
    for_cal_list = sorted(integer_list[:i+1])
    mid_idx = int(len(for_cal_list)/2)
    if len(for_cal_list)%2 == 0:
        result.append(for_cal_list[mid_idx-1])
    else:
        result.append(for_cal_list[mid_idx])

for i in result:
    print(i)