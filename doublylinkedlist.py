class Node:
  def __init__(self,data = None,next = None, prev = None):
    self.data=data
    self.next=next
    self.prev=prev

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def print_forward(self):
    # This method prints list in forward direction. Use node.next
    if(self.head == None):
      print("Linked list is empty")
      return
    itr =self.head
    liststring = ''
    while itr:
      liststring += str(itr.data)+ '-->' if itr.next else str(itr.data)
      itr=itr.next
    print(liststring)

  def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
    if(self.head == None):
         print("Linked list is empty")
         return
    itr =self.head
    liststring = ''
    while itr.next:
      itr=itr.next
    pitr = itr
    while pitr:
      liststring += str(pitr.data)+ '-->' if pitr.prev else str(pitr.data)
      pitr = pitr.prev
    print("linklist in reverse",liststring)   

  def get_length(self):
    count=0
    itr = self.head
    while itr:
      count += 1
      itr=itr.next
    return count

    
  def insert_at_begining(self, data):
    if self.head == None:
      node = Node(data, self.head,None)
      self.head=node
    else:
      node = Node(data, self.head,None)
      self.head.prev =node
      self.head = node

  def insert_at_end(self, data):
    if(self.head == None):
         self.head =Node(data,None,None)
         return
    itr=self.head
    while itr:
      if itr.next == None:
        itr.next = Node(data,None,itr)
        return
      itr = itr.next
  

  def insert_at(self, index, data):
    if index<0 or index>self.get_length():
          raise Exception("Invalid Index")
    if index == 0:
         self.insert_at_begining(data)
         return
    count = 0
    itr = self.head
    while itr: 
      if count == index-1:
        node = Node(data,itr.next,itr)
        if node.next:
          node.next.prev = node
        itr.next = node
        break
      count += 1
      itr = itr.next
    

  def remove_at(self, index):
    if index < 0 or index>self.get_length():
          raise Exception("Invalid Index")
    if index == 0:
      self.head= self.head.next
      self.head.prev = None
      return
    count = 0
    itr = self.head
    while itr:
      if count == index:
        itr.prev.next = itr.next
        if itr.next:
          itr.next.prev = itr.prev  
        break
      count +=1
      itr = itr.next
        

  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)

  def insert_after_value(self, data_after, data_to_insert):
    if self.head is None:
      return
    # if self.head.data==data_after:
    #   self.head.next = Node(data_to_insert,self.head.next)
    #   return
    
    itr = self.head
    while itr:
      if itr.data == data_after:
        node= Node(data_to_insert, itr.next, itr)
        itr.next = node
        itr.next.next.next.prev = node
        break
      itr = itr.next

  def remove_by_value(self, data):
    if self.head is None:
          return
    if self.head.data == data:
      self.head = self.head.next
      self.head.prev = None
      return
    itr = self.head
    while itr.next:
      if itr.next.data == data:
        itr.next = itr.next.next
        itr.next.next.prev = itr
        break
      itr = itr.next
        

if __name__ == 'doublylinkedlist':
  ll = DoublyLinkedList()
  ll.insert_values(["banana","mango","grapes","orange"])
  ll.print_forward()
  ll.print_backward()
  ll.insert_at_end("figs")
  ll.print_forward()
  ll.insert_at(0,"jackfruit")
  ll.print_forward()
  ll.insert_at(6,"dates")
  ll.print_forward()
  ll.insert_at(2,"kiwi")
  ll.print_forward()
  ll =  DoublyLinkedList()
  ll.insert_values(["banana","mango","grapes","orange"])
  ll.insert_at(1,"blueberry")
  ll.remove_at(2)
  ll.print_backward()
  
  ll.insert_values([45,7,12,567,99])
  ll.insert_at_end(67)
  ll.print_backward()
