graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)

"""
인접 리스트 방식은 연결된 정보만 저장해 메모리를 효율적으로 사용하지만, 
특정 두 노드가 연결되어 있는지 확인하는 것이 느리다. 
앞에서 부터 차례대로 확인해야 한다. 
"""