from copy import deepcopy
from collections import deque


def virus():
    global max_v
    temp_data = deepcopy(data)
    q = deque()
    visit = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if temp_data[i][j] == 2:
                q.append((i, j))

                visit[i][j] = 1
    while q:
        current = q.popleft()
        for a, b in dr_c:
            ni = a + current[0]
            nj = b + current[1]
            if 0 <= ni < N and 0 <= nj < M and not visit[ni][nj]:
                if temp_data[ni][nj] == 0:
                    temp_data[ni][nj] = 2
                    visit[ni][nj] = 1
                    q.append((ni,nj))
    temp = 0
    for k in range(N):
        for l in range(M):
            if temp_data[k][l] == 0:
                temp += 1
    if max_v < temp:
        max_v = temp

def solve(idx):
    if idx == 3:
        virus()
        return

    for i in range(N):
        for j in range(M):
            if data[i][j] == 0 and not visited[i][j]:
                data[i][j] = 1
                visited[i][j] = 1
                solve(idx + 1)
                data[i][j] = 0
                visited[i][j] = 0


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr_c = [(0, 1), (1, 0), (0, -1), (-1, 0)]
max_v = 0
solve(0)
print(max_v)
