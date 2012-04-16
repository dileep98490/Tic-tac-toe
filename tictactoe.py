#!/usr/bin/python
from datetime import datetime

import random
def opensquare(a,s):
    k=0
#Checking the open rows
    for i in range(0,3):
        f=0
        for j in range(0,3):
            if a[i][j]==s or a[i][j]=='#':
                f+=1
        if f==3:
            k+=1
#Checking the open columns
    for j in range(0,3):
        f=0
        for i in range(0,3):
            if a[i][j]==s or a[i][j]=='#':
                f+=1
        if f==3:
            k+=1
#Checking the good diagonal
    i=0
    j=0
    f=0
    while(i!=3):
        if a[i][j]==s or a[i][j]=='#':
            f+=1
        i+=1
        j+=1
    if f==3:
        k+=1
#Checking the bad diagonal
    i=2
    j=0
    f=0
    while(i!=-1):
        if a[i][j]==s or a[i][j]=='#':
            f+=1
        i-=1
        j+=1
    if f==3:
        k+=1
    return k
#To calculate SEF
def score(a):
    return opensquare(a,'X')-opensquare(a,'O')

def max_min_score(a,s):
    p=[]
    for i in range(0,3):
        for j in range(0,3):
            if a[i][j]=='#':
                a[i][j]=s
                f=score(a)
                if complete(a,s):
                    if s=='X':
                        f=9
                    else:
                        f=-10
                p.append([f,i,j])
                a[i][j]='#'
    #print p
    if s=='X':#We need to maximise
        max_=-10
        for i in p:
            #print 'Hello'+str(i)
            if i[0]>=max_:
                if i[0]==max_:
                    tm=datetime.now()
                    tm=tm.second/31
                    if random.randint(0,1)==1 or tm==1:
                        continue
                max_=i[0]
                f1=i[1]
                f2=i[2]#Storing the coordinates for future changing
        #print f1
        #print f2
        return f1,f2
    if s=='O':#We need to maximise
        min_=12
        for i in p:
            if i[0]<=min_:
                if i[0]==min_:
                    tm=datetime.now()
                    tm=tm.second/31
                    if random.randint(0,1)==1 or tm==0:
                        continue
                min_=i[0]
                f1=i[1]
                f2=i[2]#Storing the coordinates for future changing
        return f1,f2
    
    
#To see if it's max or min's chance and change the square as per player's advantage
def nextplay(a,f):
    if f=="max":
       f1,f2=max_min_score(a,'X')
       a[f1][f2]='X'
       return a
    if f=='min':
       f1,f2=max_min_score(a,'O')
       a[f1][f2]='O'
       return a
def complete(a,s):
#Checking the open rows
    for i in range(0,3):
        f=0
        for j in range(0,3):
            if a[i][j]==s:
                f+=1
        if f==3:
            return True
#Checking the open columns
    for j in range(0,3):
        f=0
        for i in range(0,3):
            if a[i][j]==s:
                f+=1
        if f==3:
            return True
#Checking the good diagonal
    i=0
    j=0
    f=0
    while(i!=3):
        if a[i][j]==s:
            f+=1
        i+=1
        j+=1
    if f==3:
        return True
#Checking the bad diagonal
    i=2
    j=0
    f=0
    while(i!=-1):
        if a[i][j]==s:
            f+=1
        i-=1
        j+=1
    if f==3:
        return True
    return False
            
a=[['#','#','#'],['#','#','#'],['#','#','#']]
for i in a:
    print i
#print score(a)
while True:
    print "First player's Move"
    for i in nextplay(a,'max'):
        print i
    if complete(a,'X'):
        print "First player wins"
        break
    p=0
    for i in range(0,3):
        for j in range(0,3):
            if a[i][j]=='#':
                p=1
                break
        if p==1:
            break
    if p==0:
        print "The game is tied"
        break
#print score(a)
    print "Second player's Move"
    for i in nextplay(a,'min'):
        print i
    if complete(a,'O'):
        print "Second player wins"
        break
