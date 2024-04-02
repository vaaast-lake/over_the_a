N = int(input())
test_people = list(map(int, input().split()))
B, C = map(int, input().split())
teacher = 0

for el in test_people: # ㅅㅂ 남은 학생수가 감독자 수보다 작을 수 있다는 생각을 하지 못함.;;
    check = el - B
    teacher += 1
    if check <= 0:
        continue
    if check % C == 0:
        teacher += check // C
    else:
        teacher += check // C + 1

print(teacher)