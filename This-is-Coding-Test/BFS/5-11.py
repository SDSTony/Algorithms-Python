from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

visited = []
for i in range(N):
    visited.append([0 for i in range(M)])

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    dx = [-1, 1, 0, 0] #상, 하, 좌, 우
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # oob 처리
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                visited[nx][ny] = 1
                continue
            else:
                if visited[nx][ny] == 1:
                    continue
                else:
                    graph[nx][ny] += graph[x][y] # 이전 state의 값 더해주기 
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    
    
    return graph[N-1][M-1]


print(bfs(0,0))
# print(visited)
# print(graph)
        

    
