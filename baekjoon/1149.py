# https://www.acmicpc.net/problem/1149
import sys
input = sys.stdin.readline

n = int(input())

matrix = [[0]*3 for i in range(n)]

for i in range(n):
    matrix[i][0], matrix[i][1], matrix[i][2] = map(int, input().split())

for i in range(1,n):
    matrix[i][0] = matrix[i][0] + min(matrix[i-1][1],matrix[i-1][2])
    matrix[i][1] = matrix[i][1] + min(matrix[i-1][0],matrix[i-1][2])
    matrix[i][2] = matrix[i][2] + min(matrix[i-1][0],matrix[i-1][1])

print(min(matrix[n-1][0], matrix[n-1][1], matrix[n-1][2]))

