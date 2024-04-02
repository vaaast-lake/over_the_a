from collections import deque
d_ij = ((0, 1), (0, -1), (1, 0), (-1, 0))


def dfs(lev):
    if lev == 3:
        return


def bfs(p, q):
    queue = deque([(p, q)])
    while queue:
        x, y = queue.popleft()
        for di, ij in d_ij:
            ni, nj = x + di, y + ij
            if 0 <= ni < N and 0 <= nj < M:
                if A[ni][nj] == 0:
                    A[ni][nj] = 2
                    queue.append((ni, nj))


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if A[i][j] == 2:
            bfs(i, j)
