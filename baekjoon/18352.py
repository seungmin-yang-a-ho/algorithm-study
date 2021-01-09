# https://www.acmicpc.net/problem/18352
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,k,x = map(int,input().split()) # n : 도시의 개수, m : 도로의 개수, k : 도시까지의 최단거리 , x : 출발지점

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(m):
    a, b = map(int,input().split()) 
    graph[a].append((b,1))

def getSmallestNode():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i

    return index

def dijkstra(x):
    visited[x] = True
    distance[x] = 0
    for j in graph[x]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = getSmallestNode()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(x)

result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)

if isinstance(result,list):
    for i in result:
        print(i)
else:
    print(-1)