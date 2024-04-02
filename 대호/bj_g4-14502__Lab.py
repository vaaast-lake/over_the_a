import sys
from collections import deque
sys.stdin = open('./bj_g4-14502__Lab__input.txt', 'r')

input = sys.stdin.readline
print = sys.stdout.write

FORBID = -1
VIRUS = 2
WALL = 1
PATH = 0


def bfs(cnt=1):
    copy_table = [table[i][:] for i in range(N+2)]
    q = deque()
    flag = 0
    for r in range(1, N):
        for c in range(1, M):
            if copy_table[r][c] == PATH:
                q.append((r, c))
                flag = 1
                break
        if flag:
            break

    while q:
        cur_x, cur_y = q.popleft()
        for move_x, move_y in moves:
            next_x, next_y = cur_x + move_x, cur_y + move_y
            if copy_table[next_x][next_y] == PATH:
                copy_table[next_x][next_y] = cnt + 2
                cnt += 1
                q.append((next_x, next_y))
            if copy_table[next_x][next_y] == VIRUS:
                return -1

    return cnt


def set_wall(cnt=0, start_pos=0):
    global max_v
    if cnt == 3:
        max_v = max(max_v, bfs())
        return

    for i in range(start_pos, path_cnt):
        path_x, path_y = path_pos[i]
        table[path_x][path_y] = 1
        set_wall(cnt+1, i+1)
        table[path_x][path_y] = 0


N, M = map(int, input().split())
table = [[-1] * M]
table += [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)]
table += [[-1] * M]

path_pos = []
for r in range(1, N):
    for c in range(1, M):
        if table[r][c] == PATH:
            path_pos.append((r, c))

path_cnt = len(path_pos)
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
max_v = 0

set_wall()

print(f'{max_v}')

sys.stdin.close()