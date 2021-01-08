import queue

# QUEUE
q=queue.Queue()
n=int(input("Enter elements of queue"))
for i in range(n):
    v=int(input("Enter data for queue"))
    q.put(v)
print("QUEUE: ",end=' ')
while not q.empty():
    print(q.get(),end=' ')

# STACK
L=queue.LifoQueue()
n=int(input("\nEnter number of elements of stack"))
for i in range(n):
    v=int(input("Enter data for stack"))
    L.put(v)
print("STACK: ",end=' ')
while not L.empty():
    print(L.get(),end=' ')
