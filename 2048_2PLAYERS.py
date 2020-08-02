from tkinter import *
import random
import numpy as np
import time

rows=int(input('Enter the no of rows:'))


i1=random.randint(0,rows-1)
j1 = random.randint(0,rows-1)
i2 = random.randint(0,rows-1)
j2 = random.randint(0,rows-1)

l=np.zeros([rows,rows]).astype(int)


def get_random():
    value=random.choice([2,4])
    return value

def get_random2():
    ran1 = random.randint(0, rows - 1)
    ran2 = random.randint(0, rows - 1)
    while (True):
        if l[ran1][ran2] == 0:
            l[ran1][ran2] = get_random()
            break
        ran1 = random.randint(0, rows - 1)
        ran2 = random.randint(0, rows - 1)

colours=['#ffd966','#03a9f4','#ff9800','#ff5722','#e51c23']
def Draw(L):

    for i in range(rows):
        for j in range(rows):
            if L[i][j]==0:
                col='#9e9e9e'
            elif L[i][j]>0 and L[i][j]<16 :
                col=colours[0]
            elif L[i][j]>=16 and L[i][j]<=64:
                col=colours[1]
            elif L[i][j]>64 and L[i][j]<=128:
                col=colours[2]
            elif L[i][j]>128 and L[i][j]<=1024:
                col=colours[3]
            else:
                col=colours[-1]

            if L[i][j] != 0:

                Button(win, height=1, width=3, bg=col,text=L[i][j], fg='white', font=('bold', 30), bd=2).grid(row=i,
                                                                                                                  column=j)
            else:
                Button(win, height=1, width=3,  bg=col, fg='grey', font=('bold', 30), bd=2).grid(row=i,
                                                                                                           column=j)



def create_grid1(rows):
    Draw(l)



for i in range(rows):
    for j in range(rows):
        if (i == i1 and j == j1) or (i == i2 and j == j2):
            l[i][j]=get_random()
        else:
            l[i][j]=0

def left(A):
    b = []
    for i in range(len(A)):
        if A[i] != 0:
            b.append(A[i])

    for i in range( 0,len(b)-1 ,1):
        if b[i] == b[i + 1]:
            r = b.pop(i+1 )
            b.append(0)
            b[i] = b[i] + r

    for _ in range(len(A) - len(b)):
        b.append(0)
    A=b
    print(A)
    return A

def right(A):

    b = []
    for i in range(len(A)):
        if A[i] != 0:
            b.append(A[i])
    for i in range(len(b) - 1, 0, -1):
        if b[i] == b[i - 1]:
            r = b.pop(i - 1)
            b.insert(0, 0)
            b[i] = b[i] + r
    for i in range(len(A)-len(b)):
        b.insert(0,0)
    A=b
    return A

def down1(rows):
    m = l.T
    for i in range(rows):
        m[i] = right(m[i])
    get_random2()
    create_grid1(rows)

def up1(rows):
    m=l.T
    for i in range(rows):
        m[i]=left(m[i])
    get_random2()
    create_grid1(rows)


def left1(rows):
    for i in range(rows):
        l[i]=left(l[i])
    get_random2()
    create_grid1(rows)

def right1(rows):

    for i in range(rows):
        l[i]=right(l[i])
    get_random2()
    create_grid1(rows)

win=Tk()
win.geometry('500x500+50+50')
create_grid1(rows)

while True:

    win.bind("<KeyPress-Right>",lambda e:right1(rows))
    win.bind("<KeyPress-Up>", lambda f: up1(rows))
    win.bind("<KeyPress-Down>", lambda g: down1(rows))
    win.bind("<KeyPress-Left>", lambda h: left1(rows))

    win.update()
    time.sleep(0.1)

win.mainloop()