from collections import deque

stk = deque()
print(dir(stk))

stk.append(100)
stk.append(200)
stk.append(300)
stk.append(400)
stk.pop()

print(stk)
print(len(stk))
