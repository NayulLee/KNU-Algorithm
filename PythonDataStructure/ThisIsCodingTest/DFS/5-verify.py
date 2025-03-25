# 문제 : 그래프 탐색하기
# 주어진 그래프에서 DFS와 BFS로 각 노드를 1부터 시작하여 차례대로 방문해 보세요.
# 각 탐색의 결과를 출력하는 프로그램을 작성하세요

from collections import deque

def dfs(graph, start, visitedDfs):
    visitedDfs[start] = True
    print(start, end =' ')
    for i in graph[start]:
        if not visitedDfs[i]:
            dfs(graph, i, visitedDfs)

def bfs(graph, start, visitedBfs):
    queue = deque([start]) # 큐에 집어넣는 행위를 방문하는것이라고 본다.
    visitedBfs[start] = True   # 따라서 큐에 집어넣는 구문 뒤에는 반드시 True로 바꿔주는 코드가 있어야한다.
    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v]:
            if not visitedBfs[i]:
                queue.append(i)
                visitedBfs[i] = True


graph = [[],
         [2, 3],
         [1, 4, 5],
         [1, 6],
         [2],
         [2],
         [3]
         ]

visitedDfs = [False] * 7
visitedBfs = [False] * 7

print('DFS : ', end='')
dfs(graph, 1, visitedDfs)
print('\nBFS : ', end='')
bfs(graph, 1, visitedBfs)