from collections import deque
d_ij = ((0, 1), (0, -1), (1, 0), (-1, 0))


def dfs(lev, a, arr):
    global min_v
    if lev == 3:
        cnt_v = 0
        lab = v = [x[:] for x in arr]
        for i in range(N):
            for j in range(M):
                if lab[i][j] == 1:
                    cnt_v += 1
                elif lab[i][j] == 2:
                    cnt = 0
                    queue = deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        for di, ij in d_ij:
                            ni, nj = x + di, y + ij
                            if 0 <= ni < N and 0 <= nj < M:
                                if lab[ni][nj] == 0:
                                    lab[ni][nj] = 2
                                    cnt += 1
                                    if cnt >= min_v: return
                                    queue.append((ni, nj))
                    cnt_v += cnt
                    if cnt_v >= min_v: return
        if cnt_v < min_v:
            min_v = cnt_v
        return
    for idx in range(a, N * M):
        i = idx // M
        j = idx - i * M
        if arr[i][j] == 0:
            arr[i][j] = 1
            dfs(lev + 1, idx + 1, arr)
            arr[i][j] = 0


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
init_v = 0
for i in range(N):
    for j in range(M):
        if A[i][j] == 2:
            init_v += 1
min_v = 64
dfs(0, 0, A)
result = M * N - min_v - init_v
print(str(result))
