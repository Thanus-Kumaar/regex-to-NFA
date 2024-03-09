'''
This is the representation of node of NFA

A modified doubly linked list, which can store multiple next elements
- It has stacks for storing paranthesis and 'or' pathways
- isFinal variable is set to True if it is final state
- A stack for storing paranthesised expressions
- A stack for storing multiple pathways
- Variable for storing previous address/node
'''

class ModifiedDoublyLinkedList:
  count = 0

  class Node:
    def __init__(self,number,arrow):
      self.isFinal = False
      self.nodeNumber = number
      self.arrowVal = arrow
      self.prev = None
      self.nextAdd = []
  
  def __init__(self):
    self.head = self.Node(0,"start")
    self.currPointer = self.head
    self.paranthesisStack = []
    self.orStack = []
    
  def addNode(self,alphabet):
    ModifiedDoublyLinkedList.count += 1
    self.currPointer.nextAdd.append(self.Node(ModifiedDoublyLinkedList.count,alphabet))
    for i in self.currPointer.nextAdd:
      i.prev = self.currPointer
    if(len(self.currPointer.nextAdd)==1):
      self.currPointer = self.currPointer.nextAdd[0]

  def printList(self):
    headNode = self.head
    while(headNode.nextAdd!=[]):
      print(headNode.arrowVal,"->|"+str(headNode.nodeNumber)+"|->",headNode.nextAdd)
      headNode = headNode.nextAdd[0]


mdl = ModifiedDoublyLinkedList()
mdl.addNode("a")
mdl.addNode("b")
mdl.printList()