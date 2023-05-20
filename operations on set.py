#operations on set
s=set()
print(s)

s.add(1)
s.add(1)
s.add(5)
s.add(7)          #add on element
s.add(8)
s.add(9)
s.add(4)
print(s)

print(len(s))  #length of set

s.remove(8)  #remove set of element
print(s)

s.pop()     #remove arbitary element
print(s)

s.clear()  #empty the set
print(s)
