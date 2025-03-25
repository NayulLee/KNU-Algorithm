# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현

graph = [[] for _ in range(3)] # 리스트 컴프리헨션, graph = [[], [], []]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7)) # 튜플 (1, 7)추가가, 1:연결된 노드 번호, 7:노드1과 0사이의 거리
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)