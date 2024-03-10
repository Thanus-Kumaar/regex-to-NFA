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
  
  def __init__(self,alphaSet):
    self.head = self.Node(0,"start")
    self.currPointer = self.head
    self.paranthesisStack = []
    self.orStack = []
    self.alphaSet = alphaSet
    
  def addNode(self,alphabet):
    print(alphabet,"Before adding: ",self.currPointer)
    ModifiedDoublyLinkedList.count += 1
    if(alphabet == "|"):
      self.popOrStack()
    else:
      self.pushParaStack(alphabet)
      if(alphabet!="(" or alphabet!=")"):
        self.pushOrStack(alphabet)
        
      if(alphabet=="."):
        self.currPointer.nextAdd.append(self.Node(ModifiedDoublyLinkedList.count,self.alphaSet))
      else:
        self.currPointer.nextAdd.append(self.Node(ModifiedDoublyLinkedList.count,alphabet))
      for i in self.currPointer.nextAdd:
        i.prev = self.currPointer

      if(len(self.currPointer.nextAdd)==1):
        self.currPointer = self.currPointer.nextAdd[0]
      else:
        self.currPointer = self.currPointer.nextAdd[-1]

    print("After adding: ",self.currPointer)
    
  def pushOrStack(self,data):
    self.orStack.append(data)
  
  def pushParaStack(self,data):
    self.paranthesisStack.append(data)
  
  def popOrStack(self):
    while(self.orStack!=[]):
      self.orStack.pop()
      self.currPointer = self.currPointer.prev
  
  def popParanthesisStack(self):
    pass

  def printList(self,node):
    print(node.nodeNumber,node.arrowVal)
    if(node.nextAdd==[]):
      return
    for i in node.nextAdd:
      self.printList(i)


mdl = ModifiedDoublyLinkedList()
mdl.addNode("a")
mdl.addNode("b")
mdl.addNode("|")
mdl.addNode("b")
mdl.addNode("b")
mdl.printList(mdl.head)