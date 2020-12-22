#rear of queue is at the end of the list
class QueueX:
    
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(len(self.items),item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
class Node:
    
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext
    
#implement append, index, pop, insert
class UnorderedList:
    
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current=current.getNext()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item: 
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def append(self, item): #add to end of list
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        temp = Node(item)
        temp.setNext(current.getNext())
        current.setNext(temp)
    def index(self, item):
        current = self.head
        count = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                count += 1
                current = current.getNext()
        if found == True:
            return count
        else:
            print("item not in list")
    def pop(self):#
        current = self.head
        if current.getNext() == None:
            self.head = None
        else:
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None) #pop
        return current.getData()
    def insert(self, item, index):
        new = Node(item)
        current = self.head
        previous = None
        count = 0
        while count != index and current!= None:
            count = count + 1
            previous = current
            current = current.getNext()
        if count == index:
            previous.setNext(new)
            new.setNext(current)
        elif current == None:
            print("index is past the end of list")
    def reverse(self):
        newlist = UnorderedList()
        current = self.head
        while current != None:
            newlist.add(current.getData())
            current = current.getNext()
        return newlist
    def slice(self, start, stop):
        current = self.head
        count = 0
        stop = stop - 1
        #newlist = UnorderedList()
        newlist = []
        if (start<0) or (start>stop):
            print("input error for start and stop")
        elif current == None:
            print("no item in list")
        else:
            while current != None and count != start:
                current = current.getNext()
                count += 1
            newlist.append(current.getData())
            #newlist.add(current.getData()) #ADD includes Node(item)
            while count < stop:
                current = current.getNext()
                newlist.append(current.getData())
                count += 1  
            return newlist          
    def convert(self):
        pythonlist = []
        current = self.head
        while current != None:
            pythonlist.append(current.getData())
            current = current.getNext()
        print(pythonlist)


#Implement a stack using linked lists
class stackl:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def push(self, item):
        new = Node(item)
        if self.head == None:
            self.head = new
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(new)
    def pop(self):
        current = self.head
        if current.getNext() == None:
            self.head = None
        else:
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
        return current.getData()
    def peek(self):
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        return current.getData()    


#doubly linked list: each node has a reference to the next node(next) as well as a reference to the previous node(back). The head reference also contains two references, to the first and last node in linked list.
class Deque2:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def addFront(self, item):
        new = Node(item)
        new.setNext(self.head)
        self.head = new
        self.tail = self.head
        while self.tail != None:
            self.tail = self.tail.getNext()
    def addRear(self, item):
        new = Node(item)
        if self.head == None:
            self.head = New
            self.tail = self.head
            while self.tail != None:
                self.tail = self.tail.getNext()
        else:
            self.tail = self.head
            while self.tail.getNext() != None:
                self.tail = self.tail.getNext()
            self.tail.setNext(new)
            self.tail = self.tail.getNext()
    def removeFront(self):
        removed = self.head
        self.head = self.head.getNext()
        return removed.getData()
    def removeRear(self):
        current = self.head
        self.tail = self.head
        while self.tail.getNext() != None:
            self.tail = self.tail.getNext()
        while current.getNext() != self.tail:
            current = current.getNext()
        current.setNext(None)
        removed = self.tail
        self.tail = current
        return removed.getData()
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
        
    
