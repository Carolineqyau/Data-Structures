# Recursive Functions
Date: September 7 2019  
Author: Caroline Yau  

## Functions Included
1. **frisbeeSort**: a function that expects one argument, a possibly unsorted list of numbers representing frisbees, that uses the frisbee flipping technique to sort the list. 
   - an arbitrary stack of n frisbees is represented as a python list of numbers with each number representing the size of the frisbee. When sorted, the smallest frisbee will be at index 0 in the list, and the largest frisbee will be at index n-1. 
   - frisbee flipping technique: a sorted frisbee stack is defined as having the smallest frisbee on top, the second smallest frisbee under the smallest frisbee, and so on. A shovel is the only tool that can be used to flip any top partition of the stack, including the entire stack. There only ever exists *one* stack of frisbees, not multiple smaller independent stacks. Larger frisbees may be on top of smaller frisbees and vice versa.
   
2. **bubbleSort**: a function implementing bubble sort using simultaneous assignment. 
3. **mergeSort**: a function implementing merge sort without using the slice operator. 
