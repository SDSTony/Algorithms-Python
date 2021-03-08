# queue 구현시에는 일반적으로 deque을 사용
# deque은 데이터 넣고 빼는 속도가 리스트에 비해 효율적이며, queue 라이브러리 보다 간단하다
from collections import deque
queue = deque()

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


