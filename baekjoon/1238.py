import sys
import copy
input = sys.stdin.readline

INF = 1e9

n,m,x = map(int,input().split())

# 각 마을에서 x까지와
# x에서 각 마을까지의 합

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def getSmallestNode():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(x):
    distance[x] = 0
    visited[x] = True
    for j in graph[x]:
        distance[j[0]] = j[1]
    for _ in range(n-1):
        now = getSmallestNode()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(x)
distance_x = copy.copy(distance)

distance_all = []
for i in range(1,n+1):
    visited = [False]*(n+1)
    distance = [INF]*(n+1)
    dijkstra(i)
    result_distance = distance[x]+distance_x[i]
    distance_all.append(result_distance)

distance_max = 0
for distance_item in distance_all:
    if distance_item >= INF:
        continue
    if distance_max < distance_item:
        distance_max = distance_item
    

result = distance_max
print(result)