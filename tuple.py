# creating tuple
t=1,2,3
print(t)
t=tuple('string')
print(t)

for i in t:
    print(i)

for key,i in enumerate(t):
    print(key," " ,i)
print(t[0:4])