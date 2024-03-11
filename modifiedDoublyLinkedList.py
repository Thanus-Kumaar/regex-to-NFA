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
        def __init__(self, number, arrow):
            self.isFinal = False
            self.nodeNumber = number
            self.arrowVal = arrow
            self.prev = None
            self.nextAdd = []

    def __init__(self, alphaSet):
        self.head = self.Node(0, "start")
        self.currPointer = self.head
        self.paranthesisStack = []
        self.orStack = []
        self.printCompleted = []
        self.alphaSet = alphaSet

    def addNode(self, alphabet):
        print(alphabet, "After adding: ", self.currPointer)
        ModifiedDoublyLinkedList.count += 1
        if alphabet == "|":
            self.popOrStack()
        else:
            self.pushParaStack(alphabet)
            if alphabet != "(" or alphabet != ")":
                self.pushOrStack(alphabet)

            if alphabet == ".":
                self.currPointer.nextAdd.append(self.Node(ModifiedDoublyLinkedList.count, self.alphaSet))
            else:
                self.currPointer.nextAdd.append(self.Node(ModifiedDoublyLinkedList.count, alphabet))

            if alphabet == "*":
                self.popParanthesisStack(1)
            

            for i in self.currPointer.nextAdd:
                i.prev = self.currPointer

            if len(self.currPointer.nextAdd) == 1:
                self.currPointer = self.currPointer.nextAdd[0]
            else:
                self.currPointer = self.currPointer.nextAdd[-1]

        print("Before adding: ", self.currPointer)

    def pushOrStack(self, data):
        self.orStack.append(data)

    def pushParaStack(self, data):
        self.paranthesisStack.append(data)

    def popOrStack(self):
        while self.orStack != []:
            self.orStack.pop()
            self.currPointer = self.currPointer.prev

    def popParanthesisStack(self,stepCount):
        if stepCount==1:
            self.orStack.pop()
            self.currPointer.nextAdd.append(self.currPointer.prev)
            self.currPointer = self.currPointer.prev
            self.count+=1
            self.currPointer.nextAdd.append(self.Node(ModifiedDoublyLinkedList.count, "lambda"))
            self.pushParaStack("lambda")

    def setFinalState(self):
        self.currPointer.isFinal = True

    def printList(self, node):
        print(node.nodeNumber, node.arrowVal, sep="\t")
        print()
        self.printCompleted.append(node)
        if node.nextAdd == []:
            return
        for i in node.nextAdd:
            if i not in self.printCompleted:
                if i.arrowVal == "*":
                    i.arrowVal = "lambda"
                    i.nodeNumber = i.nodeNumber - 1
                self.printList(i)

    
    def star(self,prevalp):
        if prevalp != ")":
            self.popParanthesisStack(1)