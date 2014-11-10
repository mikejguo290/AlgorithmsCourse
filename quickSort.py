import copy
f = open('week2Integers.txt','r')
week2Integers =[]
for line in f:
    week2Integers.append(int(line.strip('\n')))

def PartitionFirst(A,l,r):
    p = A[l]
    i = l+1 # i separates <p from >p, i is always 1 to the left of position of where p
            # should be. 
    j = l+1 # j separates examined from unexamined# 2!
    while j< r:
        if A[j]<p:
            A[j],A[i] = A[i],A[j]
            i +=1
        j+=1
    A[l],A[i-1] = A[i-1],A[l]
    return i-1

def PartitionLast(A,l,r):
    p = A[r-1]
    i = r -2
    j = r -2
    while j > l:
        if A[j]>p:
            A[j],A[i] = A[i],A[j]
            i-=1
        j-=1
    A[r-1],A[i+1] = A[i+1],A[r - 1]
    return i+1

def quickSortLast(Array,l,r):
    if r - l> 0: 
        comparisons = r - l - 1
        # r isn't the index of rightmost element. r = len(A)
        # is this consistent?
    else:
        comparisons = 0 

    if  r > l:
        p = PartitionLast(Array,l,r) # p denotes  position of Pivot in Array
        
        smaller = quickSort(Array,l,p) # 1 to p not inclusive
        greater = quickSort(Array,p+1,r) # p+1 to r not inclusive.
        comparisons += smaller + greater
    return comparisons

def quickSortFirst(Array,l,r):
    if r - l> 0: 
        comparisons = r - l - 1
        # r isn't the index of rightmost element. r = len(A)
        # is this consistent?
    else:
        comparisons = 0 

    if  r > l:
        p = PartitionFirst(Array,l,r) # p denotes  position of Pivot in Array
        
        smaller = quickSort(Array,l,p) # 1 to p not inclusive
        greater = quickSort(Array,p+1,r) # p+1 to r not inclusive.
        comparisons += smaller + greater
    return comparisons


def findMedian(A):
    l = A[0]
    r = A[-1]
    if len(A)%2 !=0:
        mid = A[ (len(A)-1)/2 ]
    else:
        mid = A[len

Integers = [3,2,4,0,9,2,7,1]
#Integers = [0,1,2,3,4,5,6,7]
# i expect this to have 36 comparisons with current method of partitioning.

#quickSort(Integers,0,len(Integers))
#print Integers
#quickSort(Integers,0,len(Integers))
A1 = copy.copy(week2Integers)
A2 = copy.copy(week2Integers)
print quickSortFirst(A1,0,len(A1))
print quickSortLast(A2,0,len(A2))
