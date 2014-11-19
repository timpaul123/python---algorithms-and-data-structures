#!/usr/bin/env python3

def short_bubble_sort(aList):
    swaps = True
    i = len(aList) - 1
    while i > 0  and swaps:
        swaps = False
        for j in range(i):
            if aList[j] > aList[j + 1]:
                temp = aList[j]
                aList[j] = aList[j + 1]
                aList[j + 1] = temp
                swaps = True
        i = i - 1        
    return aList


def selection_sort(aList):
    for i in range(len(aList)-1, 0, -1):
        maxSlot = 0
        for j in range(1, i + 1):
            if aList[j] > aList[maxSlot]:
                maxSlot = j
                
        temp = aList[i]
        aList[i] = aList[maxSlot]
        aList[maxSlot] = temp
        print(aList)
    return aList

def insertion_sort(aList):
    for i in range(1, len(aList)):
        current = aList[i]
        position = i
        while position > 0 and aList[position - 1] > current:
            aList[position] = aList[position - 1]
            position = position - 1
        aList[position] = current
        print(aList)
    return aList
