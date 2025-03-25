from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # deque는 반드시 반복 가능한(iterable)객체(리스트, 튜플)를 인자로 받는다.
    visited[start] = True
    while queue: # 파이썬에서는 빈 시퀀스(리스트, 튜플, 문자열 등)이 비어있으면 false, 아니면 true로 평가
        v = queue.popleft() # 큐에서 먼저 넣은 노드를 꺼내서 출력한다.
        print(v, end = ' ')
        for i in graph[v]:  # 인접 노드 탐색색
            if not visited[i]:
                queue.append(i) # 방문하지 않은 노드일 경우 queue에 집어넣는다다
                visited[i] = True

graph = [[],
         [2, 3, 8],
         [1, 7, 8],
         [4, 5],
         [5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]
         ]


visited = [False] * 9
bfs(graph, 1, visited)