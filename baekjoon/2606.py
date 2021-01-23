#https://www.acmicpc.net/problem/2606

import sys
input = sys.stdin.readline

n = int(input())
pair_num = int(input()) 
pair = [[] for i in range(n+1)]
visited = [-1]*(n+1)

for i in range(pair_num):
    j, k = map(int,input().split())
    pair[j].append(k)
    pair[k].append(j)

def getVirusCount(point):
    for i in pair[point]:
        if visited[i] != -1:
            continue
        visited[i] = 1
        getVirusCount(i)

getVirusCount(1)

print(visited.count(1)-1)
