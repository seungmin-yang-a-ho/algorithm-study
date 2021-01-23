# https://www.acmicpc.net/problem/1520
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
matrix = []
for j in range(r):
    matrix.append(list(map(int,list(input().rstrip('\n')))))

dr = [-1,1,0,0]
dc = [0,0,-1,1]

max_r = r-1
max_c = c-1

visited = [[0]*c for i in range(r)]

def dfs(start_node):
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        r = node[0]
        c = node[1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr <= max_r and 0 <=  nc <= max_c:
                if matrix[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append([nr,nc])

dfs([0,0])

print(visited[max_r][max_c]+1)