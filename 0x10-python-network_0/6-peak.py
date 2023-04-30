#!/bin/bash
"""
A function that finds a peak in a list of unsorted intergers
"""

def find_peak(list_of_intergers):
    '''
        Finds the peak in a list of numbers 
    '''
    legth = len (list_of_intergers)
    if length == 0:
        return None
    if length == 1:
        return (list_of_intergers[0])
    if length ==2:
        return list_of_intergers[0] if list_of_intergers[0] >=list_of_intergers[1] else list_of_intergers[1]

    for idx in range(0, length):
        value = list_of_intergers[idx]
        if(idx > 0 and idx < length -1 and 
                list_of_intergers[idx + 1] <= value and list_of_intergers[idx - 1] <= value):
            return value
        elif idx == 0 and list_of_intergers[idx + 1] <= value:
            return value
        elif idx == length -1 and list_of_intergers[idx -1] <= value:
            return value
        return pick
