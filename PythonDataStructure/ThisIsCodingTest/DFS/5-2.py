from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용

# 주요 메서드
# append(x) : 큐의 뒤에 x 추가
# popleft() : 큐의 앞에서 요소를 꺼낸다
# appendleft(x) : 큐의 앞에 x 추가
# pop() : 큐의 뒤에서 요소를 꺼낸다.

queue = deque() # 빈 큐 생성

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# print(queue[::-1]) 슬라이싱 기능은 제공하지 않으므로, reverse()를 이용한다.