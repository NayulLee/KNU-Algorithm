# DFS 메서드 정의
def dfs(graph, v, visited):         
    visited[v] = True   #현재 노드 방문 처리            
    print(v, end =' ') # 현재 노드 v 출력력
    
    for i in graph[v]: # 현재 노드 v와 연결된 노드를 탐색한다.
        if not visited[i]:  # 방문되지 않은 노드(False)가 있다면
            dfs(graph, i, visited)  # 방문되지 않은 노드의 인덱스를 v값으로 주고 탐색한다.

graph =[[],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
        ]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

dfs(graph, 1, visited)


# graph : 그래프를 나타내는 인접 리스트
# v : 현재 방문할 노드
# visited : 방문 여부를 체크하는 리스트
#             이 리스트의 크기는 노드의 개수에 맞춰져 있음, 초기값 False