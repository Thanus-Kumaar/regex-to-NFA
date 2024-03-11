'''

This is the representation of node of NFA

A modified doubly linked list, which can store multiple next elements
- It has stacks for storing paranthesis and 'or' pathways
- isFinal variable is set to True if it is final state
- A stack for storing paranthesised expressions
- A stack for storing multiple pathways
- Variable for storing previous address/node

'''
import networkx as nx
import matplotlib.pyplot as plt

class ModifiedDoublyLinkedList:
    
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
        self.count = 0

    def addNode(self, alphabet):
        print(alphabet, "After adding: ", self.currPointer)
        self.count += 1
        if alphabet == "|":
            self.popOrStack()
            new_node = self.Node(ModifiedDoublyLinkedList.count, alphabet)
            self.currPointer.nextAdd.append(new_node)
            new_node.prev = self.currPointer
            self.currPointer = new_node
        else:
            self.pushParaStack(alphabet)
            if alphabet != "(" or alphabet != ")":
                self.pushOrStack(alphabet)

            if alphabet == ".":
                self.currPointer.nextAdd.append(self.Node(self.count, self.alphaSet))
            else:
                self.currPointer.nextAdd.append(self.Node(self.count, alphabet))

            if alphabet == "*":
                self.popParanthesisStack(1,alphabet)

            if alphabet == "+":
                self.popParanthesisStack(1,alphabet)

            if alphabet == "?":
                self.popParanthesisStack(1, alphabet)

            for i in self.currPointer.nextAdd:
                if i != self.currPointer:
                    i.prev = self.currPointer

            if len(self.currPointer.nextAdd) == 1:
                self.currPointer = self.currPointer.nextAdd[0]
            else:
                self.currPointer = self.currPointer.nextAdd[-1]

    def pushOrStack(self, data):
        self.orStack.append(data)

    def pushParaStack(self, data):
        self.paranthesisStack.append(data)

    def popOrStack(self):
        while self.orStack != []:
            self.orStack.pop()
            self.currPointer = self.currPointer.prev

    def popParanthesisStack(self, stepCount, alphabet):
        if stepCount==1 and alphabet == "*":
            self.orStack.pop()
            self.currPointer.nextAdd.append(self.currPointer.prev)
            self.currPointer = self.currPointer.prev
            self.currPointer.nextAdd.append(self.Node(self.count, "ϵ"))
            self.pushParaStack("ϵ")

        elif stepCount==1 and alphabet == "+":
            self.orStack.pop()
            self.currPointer.nextAdd.append(self.currPointer.prev)
            self.count -= 1

        elif stepCount==1 and alphabet == "?":
            self.orStack.pop()
            self.currPointer.nextAdd.append(self.currPointer.prev)
            self.count -= 1
            self.pushParaStack("ϵ")

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
                    i.arrowVal="ϵ"
                    i.nodeNumber = i.nodeNumber - 2
                elif i.arrowVal == "+":
                    i.arrowVal="ϵ"
                    i.nodeNumber = i.nodeNumber - 2
                elif i.arrowVal== "?":
                    i.arrowVal="ϵ"
                    i.nodeNumber = i.nodeNumber - 1
                self.printList(i)

    def constructGraph(self, node, graph, visited):
        if node in visited:
            return
        visited.add(node)
        graph.add_node(node.nodeNumber, label=node.arrowVal)
        if node.nextAdd == []:
            return
        for i in node.nextAdd:
            if i != node.prev:  # Avoid creating a loop edge for the predecessor
                graph.add_edge(node.nodeNumber, i.nodeNumber, label=i.arrowVal)
            self.constructGraph(i, graph, visited)

    def visualizeGraph(self):
        graph = nx.DiGraph()
        visited = set()
        self.constructGraph(self.head, graph, visited)
        pos = nx.spring_layout(graph)
        labels = nx.get_edge_attributes(graph, 'label')
        nx.draw(graph, pos, with_labels=True, arrows=True)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        plt.show()
