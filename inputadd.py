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

    def popParanthesisStack(self):
        pass

    def setFinalState(self):
        self.currPointer.isFinal = True

    def printList(self, node):
        print(node.nodeNumber, node.arrowVal, node, node.nextAdd, sep="\n")
        print()
        if node.nextAdd == []:
            return
        for i in node.nextAdd:
            self.printList(i)

alphaSet = input()
MDL = ModifiedDoublyLinkedList(alphaSet)
regex_code = input()

for i in regex_code:
    MDL.addNode(i)

MDL.setFinalState()

MDL.printList(MDL.head)