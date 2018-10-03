

# opgave 1
### A
class A:
    def __init__(self, i = 0):
        self.i = i
    
    def m1(self):
        self.i += 1

class B(A):
    def __init__(self, j = 0):
        super().__init__(3)
        self.j = j
    
    def m1(self):
        self.i += 1
    
def main():
    b = B()             # b.i = 3  b.j = 0
    print(b.i, b.j)     #  3 0
    b.m1()              # b.i = 4  b.j = 0
    print(b.i, b.j)     #  4 0

main()



### B
class A:
    def __init__(self, i):
        self.i = i
    
    def __str__(self):
        return "I am class A"

class B(A):
    def __init__(self, i, j):
        super().__init__(i)
        self.j = j
    
    def __str__(self):
        return "I am class B"


def main():
    a = A(1)            # a.i = 3
    b = B(1, 2)         # b.i = 1   b.j = 2
    print(a)            # "I am class A"
    print(b)            # "I am class B"
    print(a.i)          # 3
    print(b.i, b.j)     # 1 2

main()


# opgave 2
#  NEE



# opgave 3
class Circle():
    PI = 3.14159265358979

    def __init__(self, straal):
        self.straal = straal
    
    def area(self, persision = 2):
        return round(self.straal * self.straal * self.PI, persision)    
    
    def perimeter(self, persision = 2):
        return round(self.straal * 2 * self.PI, persision)


c = Circle(8)
print(c.area())
# assert c.area() == 200.96
# assert c.perimeter() == 50.24
# assert c.perimeter() == 50.24




# opgave 4
class Roman():
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    @classmethod
    def roman_to_int_me(self, roman):
        return eval(self.__roman_to_int_inner(roman))

    @classmethod
    def __roman_to_int_inner(self, roman):
        if len(roman) == 1:
            return str(self.rom_val[roman])

        if self.rom_val[roman[-2]] < self.rom_val[roman[-1]]:
            return "{} - {}".format(self.rom_val[roman[-1]], self.__roman_to_int_inner(roman[:-1]))
        else:
            return "{} + {}".format(self.rom_val[roman[-1]], self.__roman_to_int_inner(roman[:-1]))

    @classmethod
    def roman_to_int(cls, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range (len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                print("+=", rom_val[s[i]], - 2 * rom_val[s[i - 1]])
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else: 
                print("+=", rom_val[s[i]])
                int_val += rom_val[s[i]]
        return int_val

# assert Roman.roman_to_int('C') == 100
assert Roman.roman_to_int('XLIX') == 49
# assert Roman.roman_to_int('MMMCMLXXXVI') == 3986


# opgave 5
class Stack:
    def __init__(_):
        _.__elements = []
        _.__index = 0
    
    # Return True if the stack is empty
    def is_empty(_):
        return _.__index == 0
    
    # Return the element at the top of the stack
    # without removing it from the stack.
    def peek(_):
        if self.is_empty():
            return none
        else:
            return _.__elements[_.__index-1]
    
    # Store an element at the top of the stack
    def push(_, value):
        if len(_.__elements) > _.__index:
            _.__elements[_.__index] = value
        else:
            _.__elements.append(value)
        _.__index += 1
        
    # Remove the element at the top of the stack and return it
    def pop(_):
        if self.is_empty():
            return none
        else:
            _.__index -= 1
            return _.__elements[_.__index]
    
    # Return the size of the stack
    def get_size(_):
        return _.__index


stack = Stack()
for i in range(10):
    stack.push(i)

while not stack.is_empty():
    # prints9 8 7 6 5 4 3 2 1 0
    print(stack.pop(), end = " ")


# opgave 6 
import time

class StopWatch():
    def __init__(_):
        _.__start_time = 0
        _.__stop_time = 0
        _.start()

    def start(_):
        _.__start_time = time.time()

    def stop(_):
        _.__stop_time = time.time()

    def get_elapsed_time(_):
        return _.__stop_time - _.__start_time

    def getStartTime(_):
        return _.__start_time

    def getStopTime(_):
        return _.__stop_time


size = 1000000
stopWatch = StopWatch()
sum = 0
for i in range(1, size + 1):
    sum += i

stopWatch.stop()
print("The loop time is", stopWatch.get_elapsed_time(), "milliseconds")



# opgave 7
# try:
#     statement1
#     statement2
#     statement3      # ALs de regel hierboven een exception gooit van wordt deze regel niet uitgevoert

# except Exception1:
#     # Handle exception

# except Exception2:
#     # Handle exception

# except Exception3:
#     # Handle exception

# finally:
#     statement4

# statement5



# opgave 8
import json, requests, sys
from pprint import pprint

# get command line arguments
# if len(sys.argv) < 2:
#     sys.exit()

# argument 0 is program name
location = ' '.join(sys.argv[1:])

# download JSON data
# api key = 842af58c3d0f07bb8fb62b5199a09350
url='http://api.openweathermap.org/data/2.5/forecast?id={}&APPID=842af58c3d0f07bb8fb62b5199a09350'.format(location)
response = requests.get(url)
response.raise_for_status()

# load JSON data into Python variable
weatherData = json.loads(response.text)

w = weatherData['list']
print(weatherData)
print(w)





# opgave 9
# ik miste alleen een dubbele enter voor de class en op 2 plekken tonden onnodige extra spaties na de code 
# ik ben wel verbaast dat mijn stuckje om self te vervangen met underscore geen problemen oplevert in pep8

import time


class StopWatch():
    def __init__(_):
        _.__start_time = 0
        _.__stop_time = 0
        _.start()

    def start(_):
        _.__start_time = time.time()

    def stop(_):
        _.__stop_time = time.time()

    def get_elapsed_time(_):
        return _.__stop_time - _.__start_time

    def getStartTime(_):
        return _.__start_time

    def getStopTime(_):
        return _.__stop_time


size = 1000000
stopWatch = StopWatch()
sum = 0
for i in range(1, size + 1):
    sum += i

stopWatch.stop()
print("The loop time is", stopWatch.get_elapsed_time(), "milliseconds")