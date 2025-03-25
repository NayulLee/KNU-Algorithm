stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()


print(stack)
print(stack[::-1]) # 슬라이싱
# start와 stop을 생략하면 전체 리스트를 대상으로 적용
# step(인덱스 이동의 간격)값이 음수이면 거꾸로 진행


