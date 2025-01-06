# s = set()
#sets cannot bhi accessed by indexes
s={9,4,7,4,4,5,8,8,4}
s.add(12)
s.add(12)
print(s, type(s))
print(len(s))
s.remove(9)
print(s)
print(s.pop())