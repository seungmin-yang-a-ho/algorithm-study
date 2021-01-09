""" 
5 6 # 정점의 갯수, 간선의 갯수
1 # 시작점
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6 
"""
import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
start_point = int(input())

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def getSmallestNode():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start_point):
    distance[start_point] = 0
    visited[start_point] = True
    for j in graph[start_point]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = getSmallestNode()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start_point)

for i in range(1,n+1):
    if distance[i] == INF :
        print("INF")
    else:
        print(distance[i])