import sys
input = sys.stdin.readline

INF = 1e9
n, m = map(int,input().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def getSmallestNode():
    min_value = INF
    index = 0
    for i in range(1, n +1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(x):
    visited[x] = True
    distance[x] = 0
    for j in graph[x]:
        distance[j[0]]=j[1]
    for i in range(n-1):
        now = getSmallestNode()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost <distance[j[0]]:
                distance[j[0]] = cost


result = [INF]
for i in range(1,n+1):
    dijkstra(i)
    print(distance)
    distance_sum = 0
    for j in distance[1:]:
        distance_sum = distance_sum + j
    result.append(distance_sum)
    distance = [INF] *(n+1)
    visited = [False] * (n+1)

answer = result.index(min(result))

print(answer)