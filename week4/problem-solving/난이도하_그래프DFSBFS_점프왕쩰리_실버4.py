# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
import sys
input = sys.stdin.readline

N = int(input())
maps = [[int(n) for n in input().split()] for _ in range(N)]
x = y = 0

def jump_king(x, y):
    if x >= N or y >= N:
        return False
    if maps[x][y] == 0:
        return False
    if maps[x][y] == -1:
        return True

    right_move = jump_king(x, y+maps[x][y]) # 오른쪽으로
    left_move = jump_king(x+maps[x][y], y) # 아래로

    return right_move or left_move 
        
print("HaruHaru" if jump_king(x, y) else "Hing")