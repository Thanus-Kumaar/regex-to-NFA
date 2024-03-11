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
            print("###",arrow)
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
        self.graph = nx.MultiDiGraph()

    def addNode(self, alphabet):
        print(alphabet, "After adding: ", self.currPointer)
        self.count += 1
        if alphabet == "|":
            self.popOrStack()
            new_node = self.Node(self.count, alphabet)
            self.currPointer.nextAdd.append(new_node)
            new_node.prev = self.currPointer
            self.currPointer = new_node
        else:
            self.pushParaStack(alphabet)
            if alphabet != "(" or alphabet != ")":
                self.pushOrStack(alphabet)

            if alphabet == ".":
                self.currPointer.nextAdd.append(self.Node(self.count, self.alphaSet))                
            elif alphabet == "*":
                self.popParanthesisStack(1,alphabet)
            elif alphabet == "+":
                self.popParanthesisStack(1,alphabet)
            elif alphabet == "?":
                self.popParanthesisStack(1, alphabet)
            else:
                self.currPointer.nextAdd.append(self.Node(self.count,alphabet))

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
            print("HOLA")
            self.currPointer.nextAdd.append(self.Node(self.count, "ϵ"))
            self.pushParaStack("ϵ")

        elif stepCount==1 and alphabet == "+":
            self.orStack.pop()
            self.currPointer.nextAdd.append(self.currPointer.prev)
            self.count -= 1

        elif stepCount==1 and alphabet == "?":
            self.orStack.pop()
            savedNode = self.currPointer
            self.currPointer = self.currPointer.prev
            self.currPointer.nextAdd.append(self.Node(self.count, "ϵ"))
            savedNode.nextAdd.append(self.currPointer.nextAdd[-1])
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

    def generate_graph(self):
        self._generate_graph_helper(self.head, set())

    def _generate_graph_helper(self, node, visited):
        if node in visited:
            return
        visited.add(node)
        self.graph.add_node(node.nodeNumber)
        for next_node in node.nextAdd:
            self.graph.add_edge(node.nodeNumber, next_node.nodeNumber, label=next_node.arrowVal)
            self._generate_graph_helper(next_node, visited)


    def visualize_graph(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
        edge_labels = {}
        for u, v, data in self.graph.edges(data=True):
            if (u, v) not in edge_labels:
                edge_labels[(u, v)] = []
            edge_labels[(u, v)].append(data['label'])

        for (u, v), labels in edge_labels.items():
            # string = ""
            # if(type(labels)==set):
            #     for i in labels[0]:
            #         string = string + 
            print(labels)
            label = ','.join(labels)
            print(label)
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels={(u, v): label})
        plt.show()

