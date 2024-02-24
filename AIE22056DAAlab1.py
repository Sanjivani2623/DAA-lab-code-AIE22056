import time 
import random

def bubble(b):
    a=b
    n=len(a)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a

def selection(b):
    a=b
    n=len(a)
    for i in range(0,n):
        max=a[0]
        pos=0
        for j in range(0,n-i):
            if a[j]>max:
                max=a[j]
                pos=j
        a[pos]=a[n-i-1]
        a[n-i-1]=max
        
    return a

def insertion(b):
    n=len(b)
    a=b
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
    

print("Enter the list of numbers separated by space")
#list1inp=input("Enter first list: ")
#list1 = list(map(int, list1inp.split()))
n=int(input("Enter number of elements in the array: "))
list1=[random.randint(1,100) for _ in range(n)]
strtBS=time.time()
bub=bubble(list1)
endBS=time.time()
timeBS=endBS-strtBS
print("Bubble sort:\n")
print('Time:',timeBS*1000,'ms')
strtsel=time.time()
sel=selection(list1)
endsel=time.time()
print("Selection sort:\n")
timeS=endsel-strtsel
print('Time:',timeS*1000,'ms')
strtI=time.time()
inst=insertion(list1)
endI=time.time()
timeI=endI-strtI
print("Insertion sort\n")
print('Time:',timeI*1000,'ms')

max_val=max(timeBS,timeI,timeS)
if max_val==timeBS:
    print("Bubble is slowest")
elif max_val==timeI:
    print("Insertion is slowest")
else:
    print("Selection is slowest")

        