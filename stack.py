from collections import deque

class Stack:
  def __init__(self):
    self.container = deque()

  def push(self,val):
    self.container.append(val)
  
  def pop(self):
    if len(self.container)==0:
      print("Stack is empty")
      return
    return self.container.pop()
  
  def peek(self):
    return self.container[-1]
    
  def size(self):
    return len(self.container)
    
  def isempty(self):
    return len(self.container) == 0

def reverse_string(s):
  string = ''
  stack = Stack()
  for c in s:
    stack.push(c)
  for i in range(stack.size()):
    string += stack.peek()
    stack.pop()
  return string
    
def is_balanced(s):
  stack = Stack()
  dict ={ ')':'(',']':'[','}':'{'}
  for c in s:
    if c == '(' or c == '{' or c == '[':
      stack.push(c)
    if c == ')' or c == '}' or c == ']':
      if stack.isempty():
        return False
      if not dict[c] == stack.pop():
        return False
  return stack.size() == 0
  
  




if __name__ == 'stack':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))