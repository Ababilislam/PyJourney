from collections import deque


queue = deque(["name", 'age', 'dob'])

print(queue)

queue.append("append")
print(queue)

queue.appendleft("left_append")

print(queue)

queue.pop()
print(queue)
queue.popleft()
print(queue)