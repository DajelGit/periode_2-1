import random
import math


# Opgave 1

array_a = [2,3,4]
array_b = ['red', 'green', 'blue']
array_c = list(range(3,5+1))
array_d = ['a', 'b', 'c', 'd']



# Opgave 2
L = [30, 1, 2, 1, 0, "hello", "Goodbye"]

L.index(1)                  # 1
L.count(1)                  # 2
len(L)                      # 7
max(L)                      # ERROR
L.append(40)                # L = [30, 1, 2, 1, 0, "hello", "Goodbye". 40]
L.insert(1, 43)             # L = [30, 43, 1, 2, 1, 0, 'hello', 'Goodbye']
L.extend([1, 43])           # L = [30, 1, 2, 1, 0, 'hello', 'Goodbye', 1, 43]
L.remove("hello")           # L = [30, 1, 2, 1, 0, 'Goodbye']
L.pop()                     # L = [30, 1, 2, 1, 0, "hello"]
"Goodbye" in L              # True
L.pop(3)                    # L = [30, 1, 2, 0, "hello", "Goodbye"]
L.sort()                    # ERROR
random.shuffle(L)           # L = [0, 'Goodbye', 'hello', 30, 1, 1, 2]



# Opgave 3
L = ['a', 'b', 'c', 'd', 'e']

L[1 : -3]                   # ['b']
L[-4 : -2]                  # ['b', 'c']
L[:3]                       # ['a', 'b', 'c']
L[:2] + L[2:]               # ['a', 'b', 'c', 'd', 'e']
L[:-1]                      # ['a', 'b', 'c', 'd']
L[::-1]                     # ['e', 'd', 'c', 'b', 'a']  
# a[start:end:step] start through not past end, by step  <-- nice
L[:]                        # ['a', 'b', 'c', 'd', 'e']



# Opgave 4
L1 = [30, 1, 2, 1, 0]
L2 = [1, 21, 13]

L1 + L2                     # [30, 1, 2, 1, 0, 1, 21, 13]
3 * L2                      # [1, 21, 13, 1, 21, 13, 1, 21, 13]
L1 > L2                     # True
[x for x in L1]             # [30, 1, 2, 1, 0]
[x for x in L1 if x in L2]  # [1]



# Opgave 5
s = 'Guido van Rossum'
l = s.split(" ")            # l = ['Guido', 'van', 'Rossum'].



# Opgave 6
### A
L = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    L[i] = L[i -1]
    print(L)

[1, 1, 3, 4, 5, 6]
[1, 1, 1, 4, 5, 6]
[1, 1, 1, 1, 5, 6]
[1, 1, 1, 1, 1, 6]
[1, 1, 1, 1, 1, 1]

### B
L1 = list(range(1, 10, 2))  # [1, 3, 5, 7, 9]
L2 = L1    # shallow copy
L1[0] = 'abc'
print(L1)  # ['abc', 3, 5, 7, 9]
print(L2)  # ['abc', 3, 5, 7, 9] <-- shallow copy

### C
a, b = 0, 1
while b < 10:
    print (b)
    a, b = b, a+b
# 1 1 2 3 5 8



# Opgave 7
palindroom_example1 = "lepel"
palindroom_example2 = "parterretrap"

def is_palindroom(string):
    string= str(string)
    x = 0
    while x < len(string) / 2:
        # print(string[x] + " != " + string[(len(string)-1)-x])
        if (string[x] != string[(len(string)-1)-x]):
            return False
        x += 1
    return True

def is_palindroom_short(string):
    length = len(str(string))
    return str(string)[0:math.ceil(length/2)] == str(string)[math.floor(length/2):length][::-1]

def is_palindroom_evenshorter(string):
    str(string) == str(string)[::-1]
    
is_palindroom("lepel")
is_palindroom("parterretrap")
is_palindroom("test")
is_palindroom("oke")


# Opgave 8




# Opgave 9




# Opgave 10