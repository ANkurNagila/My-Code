import node
class LinkedList:
    def __init__(self,head = None):
       self.head = head
       self.size = 0

    def getSize(self):
       return self.size

    def addNode(self,data):
       newNode = node.Node(data,self.head)
       self.head = newNode
       self.size+=1
       return True

    def printNode(self):
       curr = self.head
       while curr:
           print(curr.data)
           curr = curr.getNextNode()


myList = LinkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))
print("Printing")
myList.printNode()
print("Size")
print(myList.getSize())
myList.printNode()
