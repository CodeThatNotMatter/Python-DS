class HashTable:
  def __init__(self):
    self.MAX = 10
    # Chaining we use array
    self.arr =[[] for i in range(self.MAX)]
    # Linear Probing
    
  def get_hash(self,key):
    h= 0
    for char in key:
      h += ord(char)
    return h % self.MAX

  def __setitem__(self, key, val):
    h=self.get_hash(key)
    #  when there is no colision
    # self.arr[h] = val

    # When there is colision
    found = False
    for id,ele in enumerate(self.arr[h]):
      if len(ele) == 2 and ele[0]== key:
        self.arr[h][idx] = (key,val)
        found = True
        break
    if not found:
      self.arr[h].append((key, val))
    

  def __getitem__(self, key):
    h = self.get_hash(key)
    for element in self.arr[h]:
      if element[0] == key:
        return element[1]

  def __delitem__(self,key):
    h = self.get_hash(key)
    for index, ele in enumerate(self.arr[h]):
      if ele[0] == key:
        del self.arr[h][index]

t = HashTable()
t['march 6'] = 130
t['april 9']=10
t['june 26']=1
t['may 17']=78
t['january 23']=54
t['november 10']=100
t['december 9']=980
t['march 17']=345
print(t.arr) 
# print(t['march 6'])
del t['march 17']
print(t.arr)    