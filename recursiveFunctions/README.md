# Recursive Functions
Date: August 31 2019</br>
Author: Caroline Yau</br>

## Functions Included
1. **kleinfeldt**: a recursive function that takes one argument, an integer n that is greater than 0, and returns the sum of the first n terms of the kleinfeldt sequence as a real number.
   - The sum of the first n terms of the Kleinfeldt sequence is defined as  
     1 + 1/4 + 1/9 + 1/16 + 1/25 + ... + 1/n**2  
2. **ladder**: a recursive function that calculates the number of different ways one can climb to the top of a ladder with n rungs, when one can only climb one or two rungs at a time. 
   - For example, if there were three different ways to climb to the top, then the different ways are:
     1. 1 rung + 1 rung + 1 rung
     2. 1 rung + 2 rung
     3. 2 rung + 1 rung  
3. **findLargest**: a recursive function that expects one argument, a python list of integers, and returns the largest integer in the list.  
4. **findValue**: a recursive function that determines whether a given data value is in the linked list. This function returns `True` if the value is present, and `False` otherwise.  
5. **findLastValue**: a recursive function that returns the last value in a linked list.  
6. **ternarySearch**: a function that finds two midpoints that divide the list into three (hence ternary) approximately equal size segments. If the item being searched for is found at either of the midpoints, the function returns `True`.  If the item being searched for is less than the value at the first midpoint, ternary search continues with the segment to the “left” of the first midpoint. If the item being searched for is greater than the value at the second midpoint, ternary search continues with the segment to the “right” of the second midpoint. Otherwise, ternary search continues with the segment between the first and second midpoints.  
7. **ternarySearchRec**: a function that performs ternary search using recursion.

## Examples
```
>>> kleinfeldt(1)
1
>>> kleinfeldt(2)
1.25
>>> kleinfeldt(100)
1.6349839001848923
```
```
>>> ladder(3)
3
>>> ladder(5)
8
>>> ladder(10)
89
```
```
>>> findLargest([1, 7, 35, 12, 19, 106, 0])
106
>>> findLargest([42])
42
```
```
>>> n1 = Node(10)
>>> n2 = Node(20)
>>> n3 = Node(30)
>>> n4 = Node(40)
>>> n2.setNext(n1)
>>> n3.setNext(n2)
>>> n4.setNext(n3)
```
```
>>> findValue(10,n4)
True
>>> findValue(40,n4)
True
>>> findValue(50,n4)
False
```
```
>>> findLastValue(n4)
10
```
