def solve(idx, temp):
    global max_v, min_v

    if sum(data) == 0:
        if max_v < temp:
            max_v = temp
        if min_v > temp:
            min_v = temp

    
    solve(idx + 1, temp)




N = int(input())
num_list = list(map(int, input().split()))
data = list(map(int, input().split()))
max_v = -9999999999999999999999999999999999999999999999
min_v = 99999999999999999999999999999999999999999999999
solve(0, 0)

