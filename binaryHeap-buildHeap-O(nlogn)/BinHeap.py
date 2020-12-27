#1.
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    def buildHeap(self,alist): #edited buildHeap method that can sort a list in O(n log n) time: inserting n keys into the heap
        i = 0
        self.heapList = [0]
        self.currentSize = 0
        while i < len(alist):
            self.heapList.append(alist[i])
            self.currentSize = self.currentSize + 1
            self.percUp(self.currentSize)
            i += 1

#2a. Frankfurt, Mannheim, Wurzburg, Kassel, Karisruhe, Erfurt, Nurnberg, Munchen, Augsburg, Stuttgart
#2b. Frankfurt, Mannheim, Wurzburg, Kassel, Karlsruhe, Nurmberg, Erfurt, Munchen, Augsburg, Stuttgart
#2c. Frankfurt, Mannheim, Karlsruhe, Augsburg, Munchen, Nurnberg, Wurzburg, Erfurt, Stuttgart, Kassel
#2d. Frankfurt, Mannheim, Karlsruhe, Augsburg, Wurzburg, Nurnberg, Stuttgart, Erfurt, Kassel, Munchen
