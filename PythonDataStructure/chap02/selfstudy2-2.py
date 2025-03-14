# 4행 3열짜리 리스트를 생성한 후 12 ~ 1을 입력하고 출력해보자, 모든 숫자 합계도 계산

row = []
col = []
value = 12

for i in range(0, 4):
    for k in range(0, 3):
        row.append(value)
        value -= 1
    col.append(row)
    row = []

for i in range(0, 4):
    for k in range(0, 3):
        print("%d" % col[i][k], end = " ")
    print(" ")
