R, C, T = map(int, input().split())
data = [list(map(int,  input().split())) for _ in range(R)]

dr_c = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#        오른     아래      왼        위

# 1 번 미세 먼지가 이동 하도록 만든다.!!!
# 완전 탐색으로 일단 move_data에 담는다.

for tc in range(T):
    move_data = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if data[i][j] > 0:
                check = 0 # 몇번 확산 체크 위해 변수 생성
                for a, b in dr_c:
                    ni = i + a
                    nj = j + b
                    if 0 <= ni < R and 0 <= nj < C and data[ni][nj] != -1:
                        move_data[ni][nj] += data[i][j] // 5
                        check += 1
                data[i][j] -= (data[i][j] // 5) * check

    # 이게 공기 청정기 1초 이동 방향이지 싶다.
    # 그래서 이제 이렇게 이동한 값들을 본래 data배열에 담을거다.
    for i in range(R):
        for j in range(C):
            data[i][j] += move_data[i][j]
    # 이렇게 하면 한 번 이동 한거다.


    # 2번 송풍기 이동 한거 구현 해야 한다.
    check = 0
    wind_data = [[0] * C for _ in range(R)]
    for i in range(R):
        if data[i][0] == - 1:
            check += 1
            if check == 1:
                for j in range(1, C - 1): # 오른쪽
                    wind_data[i][j + 1] = data[i][j]
                for j in range(i, 0, -1): # 위
                    wind_data[j - 1][C - 1] = data[j][C - 1]
                for j in range(C - 1, 0, -1): # 왼쪽
                    wind_data[0][j - 1] = data[0][j]
                for j in range(0, i): # 아래
                    wind_data[j + 1][0] = data[j][0]
                wind_data[i][0] = - 1

            if check == 2:
                for j in range(1, C - 1): # 오른쪽
                    wind_data[i][j + 1] = data[i][j]
                for j in range(i, R - 1): # 아래
                    wind_data[j + 1][C - 1] = data[j][C - 1]
                for j in range(C - 1, 0, -1): # 왼쪽
                    wind_data[R - 1][j - 1] = data[R - 1][j]
                for j in range(R-1, i, -1): # 위
                    wind_data[j - 1][0] = data[j][0]
                wind_data[i][0] = - 1

    # 이제 바람이 이동한 데이터를 원래 데이터에 이동시켜 준다.
    check = 0
    for i in range(R):
        if data[i][0] == -1:
            check += 1
            if check == 1:
                data[i] = wind_data[i] # 오른
                for j in range(i, -1, -1):  # 위
                    data[j][C - 1] = wind_data[j][C - 1]
                data[0] = wind_data[0] # 왼쪽
                for j in range(0, i + 1):  # 아래
                    data[j][0] = wind_data[j][0]

            if check == 2:
                data[i] = wind_data[i] # 오른
                for j in range(i, R): # 아래
                    data[j][C - 1] = wind_data[j][C - 1]
                data[R - 1] = wind_data[R - 1] # 왼쪽
                for j in range(R-1, i - 1, -1): # 위
                    data[j][0] = wind_data[j][0]


temp = 0
for i in range(R):
    for j in range(C):
        temp += data[i][j]
# print(data)
print(temp + 2)

