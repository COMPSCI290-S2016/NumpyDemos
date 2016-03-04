def doSquare(i):
    return i**2

x = []
for i in range(20):
    if i % 2 == 0:
        continue
    x.append(doSquare(i))

#Do a "list comprehension"
x = [doSquare(val) for val in x]
print x
