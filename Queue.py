from collections import deque
import threading
import time
class Queue:
  def __init__(self):
    self.buffer = deque()

  def enqueue(self, val):
    self.buffer.appendleft(val)

  def dequeue(self):
    if len(self.buffer)==0:
      print("Queue is empty")
      return
    return self.buffer.pop()

  def isempty(self):
    return len(self.buffer) == 0

  def size(self):
    return len(self.buffer)



# //////////////////////////////////Question 1/////////////////////////////////////////
# po = Queue()

# def placeOrder(orders):
#   for n in orders:
#     print("Placing order", n)
#     po.enqueue(n)
#     time.sleep(0.5)
  
# def serveOrder():
#   time.sleep(1)
#   while not po.isempty():
#   # while True:
#     print("Serving Order",po.dequeue())
#     time.sleep(2)

# orders = ['pizza','samosa','pasta','biryani','burger']
# t1 =threading.Thread(target=placeOrder, args=(orders,))
# t2 =threading.Thread(target=serveOrder)

# t1.start()
# t2.start()
# t1.join()
# t2.join()


# ///////////////////////default run/////////////////////////////////////////////////
# pq = Queue()

# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.01 AM',
#     'price': 131.10
# })
# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.02 AM',
#     'price': 132
# })
# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.03 AM',
#     'price': 135
# })

# print(pq.size())


# Question 1


orders = ['pizza','samosa','pasta','biryani','burger']
t1 =threading.Thread(target=placeOrder, args=(po,orders,))
t2 =threading.Thread(target=serveOrder, args=(po,))

t1.start()
t2.start()
t1.join()
t2.join()