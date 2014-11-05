#!/usr/bin/env python3
def mergesort(alist):
    if len(alist) > 1:
        midpoint = len(alist) // 2
        leftHalf = alist[midpoint:]
        rightHalf = alist[:midpoint]
        
        mergesort(leftHalf)
        mergesort(rightHalf)
    
        i = 0
        j = 0
        k = 0
    
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                alist[k] = leftHalf[i]
                i = i + 1
            else:
                alist[k] = rightHalf[j]
                j = j + 1
            k = k + 1
        
        while i < len(leftHalf):
            alist[k] = leftHalf[i]
            i = i + 1
            k = k + 1
    
        while j < len(rightHalf):
            alist[k] = rightHalf[j]
            j = j + 1
            k = k + 1
        

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)
    
def partition(alist, first, last):
    #Take the median of the first, middle and last items in the list for the pivot
    #value to avoid efficiency diminishing to O(n^2)
    middle = (first + last)//2
    items = sorted([(aList[first], first), (aList[middle], middle), (aList[last], last)])
    (pivotValue, pivot) = items[1]
    temp = aList[first]
    aList[first] = aList[pivot]
    aList[pivot] = temp
    
    pivotValue = alist[first]
    leftMark = first + 1
    rightMark = last
    finished = False
    
    while not finished:
        
        while leftMark <= rightMark and alist[leftMark] <= pivot:
            leftMark = leftMark + 1
            
        while rightMark >= leftMark and alist[rightMark] >= pivot:
            rightMark = rightMark - 1
        
        if rightMark < leftMark:
            finished = True
        else:
            temp = alist[leftMark]
            alist[leftMark] = alist[rightMark]
            alist[rightMark] = temp
    
    temp = alist[first]
    alist[first] = alist[rightMark]
    alist[rightMark] = temp
    
    return rightMark
