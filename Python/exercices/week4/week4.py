"""

# opgave 1

from tkinter import *
from random import randint
import time

class Plot:
    def __init__(_):
        s = 1
        x2 = 50
        y2 = _.__value_to_y(randint(0,100))
        _.__setup()

    def __value_to_y(val):
        return 550-5*val
    
    def __setup():
        root = Tk()
        root.title('simple plot')

        canvas = Canvas(root, width=1200, height=600, bg='white') # 0,0 is top left corner
        canvas.pack(expand=YES, fill=BOTH)

        Button(root, text='Quit', command=root.quit).pack()

        canvas.create_line(50,550,1150,550, width=2) # x-axis
        canvas.create_line(50,550,50,50, width=2)    # y-axis


    def step():
        global s, x2, y2  # We halen hier de waardes uit de global scope zodat python niet opnieuw 
                        # copie"en van de variabelen in het geheugen rond gaat gooien. 
                        # Deze regel is dus niet verplicht maar wel een goede optimalisatie
        if s == 23:
            # new frame
            s = 1
            x2 = 50
            canvas.delete('temp') # only delete items tagged as temp
        x1 = x2
        y1 = y2
        x2 = 50 + s*50
        y2 = __value_to_y(randint(0,100))
        canvas.create_line(x1, y1, x2, y2, fill='blue', tags='temp')
        # print(s, x1, y1, x2, y2)
        s = s+1
        canvas.after(300, step)
    
    def start():
        # x-axis
        for i in range(23):
            x = 50 + (i * 50)
            canvas.create_line(x,550,x,50, width=1, dash=(2,5))
            canvas.create_text(x,550, text='%d'% (10*i), anchor=N)
            
        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            canvas.create_line(50,y,1150,y, width=1, dash=(2,5))
            canvas.create_text(40,y, text='%d'% (10*i), anchor=E)

        canvas.after(300, step) 
        root.mainloop()




# opgave 2

import json
from pprint import pprint

with open('books.json') as f:
    books = json.load(f)


### A
def avg_python_price(books):
    value, count = (0,0)
    for book in books:
        if book["topic"] == "Python":
            value += book["price"]
            count += 1

    return format(value / count, '.2f')

print(avg_python_price(books))


### B
def sorted_result(books):
    return sorted(books, key=lambda x: x["author"].split(" ")[-1:])

pprint(sorted_result(books))

"""


# opgave 3
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

def show_result():
    analyze_file(filename.get())

def analyze_file(filename):
    try:
        infile = open(filename, "r")
    
        # your code
        counts = {0 : 3, 1 : 7, 2 : 5}

        # display a histogram for counts
        show_histogram(counts)
    except IOError:
        tkinter.messagebox.showwarning("Analyze File", "File " + filename + " does not exist") 

def open_file(): 
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)
        
def show_histogram(counts): 
    numberOfBars = len(counts)
    width = int(canvas["width"])
    height = int(canvas["height"])
    heightBar = 0.75 * height
    widthBar = width - 20
    maxCounts = max(counts)
    
    for i in range(numberOfBars):
        canvas.create_rectangle(i * widthBar / numberOfBars + 10, height - 20 - counts[i] * heightBar / maxCounts, (i + 1) * widthBar / numberOfBars + 10, height - 20)
        canvas.create_text(i * widthBar / numberOfBars + 10 + 0.5 * widthBar / numberOfBars, height - 10, text = chr(i + ord('a')))
    
window = Tk()
window.title("Words Frequency Histogram")

frame1 = Frame(window)
frame1.pack()
canvas = Canvas(frame1, width = 500, height = 200)
canvas.pack()

frame2 = Frame(window)
frame2.pack()

Label(frame2, text = "Enter a filename: ").pack(side = LEFT)
filename = StringVar()
Entry(frame2, width = 40, textvariable = filename).pack(side = LEFT)
Button(frame2, text = "Browse", command = open_file).pack(side = LEFT)
Button(frame2, text = "Show Result", command = show_result).pack(side = LEFT)

window.mainloop()
