
# Using List Data Structure in Python
print("STACK USING LISTS")
stack=[]
n=int(input("enter the no. of elements of stack"))
for i in range(n):
    v=int(input("enter data"))
    stack.append(v)
print("Stack=",stack[::-1])
print("Top of stack:",stack.pop(),'\n')

# Using Collections Module
print("STACK USING COLLECTIONS.DEQUE")
from collections import deque
stack=deque()
n=int(input("enter n"))
for i in range(n):
    v=int(input("enter data"))
    stack.append(v)
print(stack)
print("Top of Stack:",stack.pop(),'\n')

# using Queue Module
print("STACK USING QUEUE MODULE") 
from queue import LifoQueue
n=int(input("Enter no. of elements of stack"))
stack=LifoQueue(n)
print("Initial Size Of Stack: ",stack.qsize())
for i in range(n):
    v=int(input("Enter data"))
    stack.put(v)

print("Is Stack Full: ",stack.full())
print("Current Size of Stack: ",stack.qsize())
print("Top Of Stack:",stack.get())
print('\n\n\n')
print(dir(LifoQueue))
