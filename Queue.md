# Queue

## Question About the Data Structure

### What is the purpose of the data structure?
Queue are very simimlar to stack. They are a linear data structure that set up data as frist in first out. So for the best example is first come frist serve in real life. So the purpose of this data structure is to set up data so there is a very distine order in how the data is used. A case I can think about is how you see a recept. The order is printed in is the frist item scanned to the last one in that order.
### What is the performance of the data structure(Big O)?
In python the Enqueue is O(1), Dequeue O(1), Front O(1), Rear O(1). Over all most thing in most laguages are just O(1) for anything with Queue
### What kind of problems can be solved using the data structure?
A example if any problem were the data needs to need to be handled in the order witch it was received.
### How would the data structure be used in Python(recursion)?
You can Implementate a using list, collections.deque, and queue.Queue. 
1. List
```python
# Initializing a queue
queue = []

# Adding elements to the queue
queue.append(1)
queue.append(2)

# Removing elements from the queue
queue.pop(0)
```
2. collections.deque
```python
from collections import deque
# Initialing a queue
queue = deque()

# Adding elements to a queue
queue.append(1)
queue.append(2)

# Removing elements from a queue
queue.popleft()
queue.popleft()

```
3. queue.Queue
```python
from queue import Queue

# Initializing a queue
q = Queue(maxsize = 5)

# Adding element to queue
q.put(1)
q.put(2)

# Removing element from queue
q.get()
q.get()


```

### What kind of errors are common when using the data structure?
If a queue has a max size you can max out a queue size and cause an error
### What is the difference between a Stack and a queue?
A Stack Is last-in, first-out as a queue is first in , first out
### Why are the difference between a stack and queue important?
The difference between gives us to comnication between a computer and how we design software depening on our need.
### What is and what are the benefits of a Circular Queue?
A Circular Queue is a version of a queue where teh last emement of the queue is connected to the first element of the queue forming a circle

## Skills

### Sorting an Queue
```python
from queue import Queue
def find_min(q, sIndex):
    minI = -1
    minv = 999999
    for i in range(sIndex):
        curr = q.queue[0]
        q.get()

        if curr <= minv and i <= sIndex :
            minI = i
            minv = curr
        q.put(curr)

    return minI
def put_in_Rear(q, minI):
    minv = None
    n = q.qsize()
    for i in range(n):
        curr = q.queue[0]
        q.get()
        if i not minI:
            q.put(curr)
        else:
            minv = curr
    q.put(minv)

def sortQueue(q):
    for i in range(1, q.qsize()+1):
        min_index = find_min(q, q.qsize() - i)
        put_in_Rear(q, min_index)

q = Queue()
q.put(34)
q.put(32)
q.put(35)
q.put(3)
q.put(23)

sortQueue(q)
for s in range(q.qsize()):
    print(q.get())
```
### Know how to use a queue with a linked list

```python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def isEmpty(self):
        return self.front == None

    def EnQueue(self, item):
        temp = Node(item):

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
    
    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None

q = Queue()
q.EnQueue(10)
q.EnQueue(23)
q.EnQueue(12)
q.DeQueue()

```
### Design Circular Queue
```python
class CircularQueue():
    def __init__(self,size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1
    def enqueue(self,data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    
    def display(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.rear >= self.front:
            print("Elements in the circular queue are: ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
            print()
        else: 
            print("Elements in Circular Queue are: ")

            for i in range(self.front, self.size):
                print(self.queue[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end = " ")
            print()

        if (self.rear +1) % self.size == self.front:
            print("Queue is Full")

cq = CircularQueue(6)
cq.enqueue(14)
cq.enqueue(56)
cq.enqueue(19)
cq.enqueue(-9)
cq.display()
cq.dequeue()
cq.dequeue()
cq.enqueue(7)
cq.display()

```
## Example Problem
Math with a queue
```python
    from queue import Queue

    def sum_of_queue(q):
        value = 0
        for s in range(5):
            value+=q.queue[0]
            q.get()
        return value

    q1 = Queue()
    q1.put(12)
    q1.put(17)
    q1.put(3)
    q1.put(4)
    q1.put(9)

    print(sum_of_queue(q1))

```
## Student Problem
You have two queue. Both are just numbers. Now you need to find the mathmatical opration set that shows if thay past a  test or not. 
```python
from queue import Queue


def test(key,q):
    did_it_pass = False
    key_number1 = 0
    key_number2 = 0
    

    q_number1 = 0
    q_number2 = 0

   # your code here

    try:
        key_final_number = key_number1 / key_number2
        q_final_number = q_number1 / q_number2
        if key_final_number == q_final_number and key_final_number != 0:
            did_it_pass = True
    except:
        i = 0
    
        return did_it_pass
key = Queue()
key.put(int(23))
key.put(4)
key.put(5)
key.put(23)
key.put(-10)

q1 = Queue()
q1.put(12)
q1.put(17)
q1.put(3)
q1.put(4)
q1.put(9)

q2 = Queue()
q2.put(3)
q2.put(6)
q2.put(7)
q2.put(12)
q2.put(15)

q3 = Queue()
q3.put(50)
q3.put(-8)
q3.put(-10)
q3.put(14)
q3.put(-27)


print(test(key,q1))
# True
print(test(key,q2))
# False
print(test(key,q3))
#True
```
[Solution](Queue_Student_Problem_Solution.py)
