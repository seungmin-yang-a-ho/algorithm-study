# https://www.acmicpc.net/problem/1520
import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

r, c = map(int, input().split())

matrix = []
for i in range(r):
    temp = list(map(int,input().split()))
    matrix.append(temp)

dc = [-1,1,0,0]
dr = [0,0,-1,1]

max_r_idx = r-1
max_c_idx = c-1

visited = [[-1]*c for i in range(r)]

def search(r,c):
    if r == max_r_idx and c == max_c_idx :
        return 1
    if visited[r][c] != -1:
        return visited[r][c]
    visited[r][c] = 0
    for i in range(4):
        move_r = r + dr[i]
        move_c = c + dc[i]
        if 0 <= move_c <=  max_c_idx and 0<= move_r <= max_r_idx:
            if matrix[move_r][move_c] < matrix[r][c]:
                visited[r][c] += search(move_r,move_c)

    return visited[r][c]


start_r = 0
start_c = 0
print(search(start_c,start_r))
