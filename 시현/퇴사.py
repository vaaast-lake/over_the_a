def solve(idx, temp):
    global max_v

    if idx >= N: # 범위 넘어서면 최댓값 반환하고 종료
        if max_v < temp:
            max_v = temp
            return
        return

    solve(idx + 1, temp) # 1추가 할까 말까 정해줌
    if idx + data[idx][0] <= N: # 추가시 범위 안이면 더하고 아니면 안더함
        solve(idx + data[idx][0], temp + data[idx][1])
    else:
        solve(idx + data[idx][0], temp)


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
solve(0, 0)
print(max_v)

