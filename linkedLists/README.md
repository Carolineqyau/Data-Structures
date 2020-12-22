# Linked Lists
Date: August 24 2019</br>
Author: Caroline Yau</br>

## Classes Included
1. **QueueX**: Queue ADT implemented with a Python list where the rear of the queue is at the end of the list. 
2. **Node**
3. **UnorderedList**: 
   - functions *append*, *index*, *pop* and *insert* are implemented. 
   - A *slice* method is implemented which takes two parameters: `start` and `stop` and returns a copy of the list starting at the `start` position and going up to but not including the `stop` position. 
   - A *convert* method is also implemented which converts an instance of the Unordered List class to an ordinary Python list.
     - ###### Example  
     If the Unordered List `x` contained the elements `10`, `20`, and `30`, `x.convert()` would return `[10, 20, 30]`.
4. **stackl**: a stack using singly linked lists where each node has a single reference to the next node in sequence.
5. **Deque2**: deque ADT implemented with a doubly linked list where each node has a reference to the next node (next) as well as a reference to the preceding node (back). The head reference also contains two references, one to the first node in the linked list and one to the last. 
