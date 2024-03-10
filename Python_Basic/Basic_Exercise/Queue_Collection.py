from collections import deque

queue = deque()

queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)

print(queue)

queue.pop()
print(queue)