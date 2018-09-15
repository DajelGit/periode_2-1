

# opgave 1
### A
tup1 = (1,2,3,4,5)
tup2 = (5,)

print(tup1, tup2)

### B
tup = ('xx', 'yy','zz')
for x in tup: print (x)

### C
tup1 = (4, 6, 2, 8, 3, 1)
tup1 = list(tup1)
tup1.insert(2, 100)
tup1 = tuple(tup1)
print(tup1)

tup1 = (4, 6, 2, 8, 3, 1)
tup1 = tup1[:2] + (100,) + tup1[2:]
print(tup1)

### D
tup = ('a', 'b', 'c')
print( "".join(tup) )

### E
L = [5, 10, 7]
print( tuple(L) )

### F
L = [(1,2), (3,4), (8,9)]
print( list(zip(*L)) )

### G
L = [ ("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("y", 3) ]
di = {}
for a, b in L: 
    di.setdefault(a, []).append(b) 
print(di)
