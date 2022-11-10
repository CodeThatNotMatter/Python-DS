import string
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


print("from example",
    least_difference(1, 10, 100),
    # least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)
# def isAnagram():
#     s='adcf'
#     t='fgea'
#     for x in string.ascii_lowercase:
#           print (x)
#           if s.count(x) != t.count(x):
#                 print(False)
#     print(True)

'''
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
      msg +=char 
print(msg, end='')        

squares = []
for n in range(10):
    squares.append(n**2)
print(squares)


triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print(triplequoted_hello == 'hello\nworld')
'''
