from tkinter import *
import random
import numpy as np
import time


#time.sleep(5)
Speed =9
rows =4    #int(input('Enter the no of rows:'))

i1 = random.randint(0, rows - 1)
j1 = random.randint(0, rows - 1)
i2 = random.randint(0, rows - 1)
j2 = random.randint(0, rows - 1)

L = np.zeros([rows, rows]).astype(int)
L2=L
L3=L


###############                     BOT  ALGORITHIUM                           ################

def get(l):
    hsum = 0
    hsize=0
    for e in l:
        if e !=0:
            hsize=hsize+1
    i=0
    while(i<=4):
        for j in range(i+1,rows):

            if (l[i]==l[j]) or (l[j]==0 ):
                if l[j]==0:
                    continue
                else:
                    hsum=hsum+2*l[i]
                    hsize=hsize-1
                    i=j
                    break
            elif (l[i]!=l[j]):
                break
        i=i+1
    return [hsize,hsum]


def HVV(l):
    h_score=0
    h_size=0

    for i in range(rows):
        a=get(l[i])
        h_score=a[1]+h_score
        h_size=h_size+a[0]

    return h_size+1

def future():
    global L2,L3

    if random.choice([1,2])==1:
        L2=right1(L2,rows,0)
    else:
        L2=left1(L2,rows,0)

    if random.choice([3,4])==3:
        L3=up1(L3,rows,0)
    else:
        L3=down1(L3,rows,0)


##                                                                                             ##

def get_random():
    value = random.choice([2, 4])
    return value

def Size(l):
    count=0
    for i in range(rows):
        for j in range(rows):
            if l[i,j]!=0:
                count=count+1
    return count

def get_random2(l):
    ran1 = random.randint(0, rows - 1)
    ran2 = random.randint(0, rows - 1)
    while (True):
        if l[ran1][ran2] == 0:
            l[ran1][ran2] = get_random()
            break
        ran1 = random.randint(0, rows - 1)
        ran2 = random.randint(0, rows - 1)

bv=0


colours=['#ffd966','#03a9f4','#ff9800','#ff5722','#e51c23']
def Draw():

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

def create_grid1():
    global L2,L3,bv,hor1,hor2,ver1,ver2
    print("__________###########_____________\n",L)

    # Add the No of Futures You want To see
    for _ in range(8):
        future()

    if hor1<ver1:
        v1=hor1
    else:
        v1=ver1
    if hor2<ver2:
        v2=hor2
    else:
        v2=ver2

    if v1<=v2:
        bv = random.choice([1, 2])
    else:
        bv = random.choice([3, 4])


    # Hash The Below Line To Have a See in the Console
    Draw()


for i in range(rows):
    for j in range(rows):
        if (i == i1 and j == j1) or (i == i2 and j == j2):
            L[i][j] = get_random()
        else:
            L[i][j] = 0


##                                       Calculatones Based On  the Move                                             ##
def left(A):
    b = []
    for i in range(len(A)):
        if A[i] != 0:
            b.append(A[i])

    for i in range(0, len(b) - 1, 1):
        if b[i] == b[i + 1]:
            r = b.pop(i + 1)
            b.append(0)
            b[i] = b[i] + r

    for _ in range(len(A) - len(b)):
        b.append(0)
    A = b
    return A

con=0
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
    for i in range(len(A) - len(b)):
        b.insert(0, 0)
    A = b
    return A

def down1(l,rows,called):
    global hor2,ver2
    m = l.T
    for i in range(rows):
        m[i] = right(m[i])
    if called == 0:

        hor2 = HVV(L3)
        ver2 = HVV(L3.T)
        return L3

    else:
        get_random2(l)
        create_grid1()


def up1(l,rows,called):
    global hor2,ver2
    m = l.T
    for i in range(rows):
        m[i] = left(m[i])
    if called == 0:
        hor2 = HVV(L3)
        ver2 = HVV(L3.T)
        return L3
    else:
        get_random2(l)
        create_grid1()


def left1(l,rows,called):
    global hor1,ver1
    for i in range(rows):
        l[i] = left(l[i])
    if called == 0:
        hor1 = HVV(L2)
        ver1 = HVV(L2.T)
        return L2
    else:
        get_random2(l)
        create_grid1()


def right1(l,rows,called):
    global hor1, ver1
    for i in range(rows):
        l[i] = right(l[i])
    if called==0:

        hor1 = HVV(L2)
        ver1 = HVV(L2.T)
        return L2

    else:

        get_random2(l)
        create_grid1()



win = Tk()
win.geometry('500x500+300+250')
create_grid1()
#time.sleep(5)
t=10**(-Speed)


while True:
    if Size(L)>=rows**2:
        break
    if bv==1:
        con=0
        win.bind("<KeyPress-Right>", right1(L,rows,1))
        time.sleep(t)
    if bv==3:
        con = 0
        win.bind("<KeyPress-Up>", up1(L,rows,1))
        time.sleep(t)
    if bv==4:
        con = 0
        win.bind("<KeyPress-Down>",down1(L,rows,1))
        time.sleep(t)
    if bv==2:
        con = 0
        win.bind("<KeyPress-Left>",  left1(L,rows,1))
        time.sleep(t)
    win.update()

win.mainloop()