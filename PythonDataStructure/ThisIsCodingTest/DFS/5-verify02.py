# BFS와 DFS를 이용하여 경로를 찾는 프로그램
# 경로가 존재하면 yes, 존재하지 않으면 no를 출력하는 프로그램을 작성하세요. 


# 1. DFS 풀이이
visitedDfs = [False] * 7

def dfs(graph, start, visited):
    if start == 6:
        return True
    visitedDfs[start] = True
    for i in graph[start]:
        if not visitedDfs[i]:
            if dfs(graph, i, visitedDfs):
                return True
    return False           

graph = [[],
         [2, 3],
         [1, 4, 5],
         [1, 6],
         [2],
         [2],
         [3]
         ]


if dfs(graph, 1, visitedDfs):
    print("Yes")
else:
    print("No")
    
# 2. BFS 풀이
from collections import deque

visitedBfs = [False] * 7

def bfs(graph, start, visitedBfs):
    queue = deque([start])
    visitedBfs[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i == 6:
             return True
            if visitedBfs[i] == False:
              queue.append(i)
              visitedBfs[i] = True
    return False          

if bfs(graph, 1, visitedBfs):
    print("Yes")
else:
    print("No")