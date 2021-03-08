"""
일반적으로 bfs가 dfs보다 조금 빠르다. 

Time complexity: O(N), N은 노드의 개수
"""

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # initiate deque with start

    visited[start] = True

    while queue:

        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
