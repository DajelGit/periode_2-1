import collections


"""
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



# opgave 2
d = {"red":4, "blue":1, "green":14, "yellow":2}

### A
d['red'] = d['blue']        #  d = {"red":1, "blue":1, "green":14, "yellow":2}

### B
d['blue'] += 10             #  d = {"red":4, "blue":11, "green":14, "yellow":2}

### C
d['yellow'] = len(d)        #  d = {"red":4, "blue":1, "green":14, "yellow":4}

### D
d['green'] = {'orange' : 6} #  d = {"red":4, "blue":1, "green":{'orange' : 6}, "yellow":2}

### E
d = dict.fromkeys(d, 0)     #  d = {"red":0, "blue":0, "green":04, "yellow":0}

### F
d.pop('black', None)        #  None  d = {"red":4, "blue":1, "green":14, "yellow":2}

### G
d.get('black', None)        #  None  d = {"red":4, "blue":1, "green":14, "yellow":2}

### H
d.setdefault('black', None) #  None  d = {"red":4, "blue":1, "green":14, "yellow":2, 'black': None}

### I
d = {}                      #  d = {}



# opgave 3
### A
d = {'c':1, 'b':2, 'a':3, 'e':1, 'd':3}
for k in sorted(d):
    print(k, d[k])

### B
D = {'a':1, 'b':2, 'c':3, 'd':1, 'e':3, 'f': 5}
print(set(d))

### C
TODO: this

### D
TODO: this

### E
TODO: this



# opgave 4
s1 = {1, 4, 5, 6}
s2 = {1, 3, 6, 7}

### A
print(s1 & s2)

### B
print(s1 ^ s2)

### C
L = [1, 7, 4, 8, 9, 9, 4, 1, 4, 11, 14, 21, 15, 5, 2, 5]
needle = {15, 11}
print(len(needle & set(L)) == len(needle))




# opgave 5
### A
t = "Mooi"
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

print(list("mooi".upper()))
print([x.capitalize() for x in t])

### B
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print([x for x in t if x.isupper()])



# opgave 6


### A
def unique_list(L):
    return list(set(L))

L = [1,2,3,3,3,3,4,5]
print(unique_list(L))


### B
def even_elements(L):
    return [x for x in L if x % 2 == 0]

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_elements(L))


### C
def is_pangram(str):
    return set("abcdefghijklmnopqrstuvwxyz") - set(str.lower()) == set()

print(is_pangram("Filmquiz bracht knappe ex-yogi van de wijs"))
"""



### D TODO: this
def sd(dict):
    return 0




# opgave 7

# modc.py wordt meerdere malen geimporteert




###################
#    opgave 8     # TODO: this
###################

from random import randint
BOARD_SIZE = 4
NR_GUESSES = 4

#initializing board
board = []
for x in range(BOARD_SIZE):
    board.append(["O"] * BOARD_SIZE)

def print_board(board):
    for row in board:
        print (" ".join(row))

#start the game and printing the board
print ("Let's play Battleship!")
print_board(board)
#define where the ship isship_

row = randint(0, BOARD_SIZE-1)
ship_col = randint(0, BOARD_SIZE-1)

"""
    here your code :
    -ask the user for a guess
    -if the user's right, the game ends
    -warn if the guess is out of the board
    -warn if the guess was already made
    -if the guess is wrong, mark the point with an X and start again
    -print turn and board again here
"""
    
if turn == NR_GUESSES-1:
    print ("Game Over")
