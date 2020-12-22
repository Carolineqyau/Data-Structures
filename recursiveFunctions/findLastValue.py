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

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n2.setNext(n1)
n3.setNext(n2)
n4.setNext(n3)

def findLastValue(node):
    if node.getNext() == None:
        return node.getData()
    else:
        return findLastValue(node.getNext())
