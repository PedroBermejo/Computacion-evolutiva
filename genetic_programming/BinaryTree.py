from collections import deque

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

    def __str__(self):
        return str(self.v)

class Tree:
    def __init__(self):
        self.root = None

    def createFromList(self, data):
        n = iter(data)
        self.root = Node(next(n))
        fringe = deque([self.root])
        while True:
            head = fringe.popleft()
            try:
                head.l = Node(next(n))
                fringe.append(head.l)
                head.r = Node(next(n))
                fringe.append(head.r)
            except StopIteration:
                break                

    def find(self, val):
        if(self.root != None):
            found = [None]
            self._find(val, self.root, self.root, found)
            return found[0]
        else:
            return None

    def _find(self, val, node, parent, found):
        if(node != None):
            if(val is node):
                found[0] = parent
            self._find(val, node.l, node, found)
            self._find(val, node.r, node, found)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)
        print()

    def _printTree(self, node):
        if(node != None):
            print(node.v, end=" "),
            self._printTree(node.l)
            self._printTree(node.r)

    def createEcuation(self):
        if(self.root != None):
            ecuation = ['']
            self._createEcuation(self.root, ecuation)
            return ecuation[0]
        else:
            return None

    def _createEcuation(self, node, ecuation):
        if(node != None):
            ecuation[0] = ecuation[0] + '('
            self._createEcuation(node.l, ecuation)
            ecuation[0] = ecuation[0] + node.v
            self._createEcuation(node.r, ecuation)
            ecuation[0] = ecuation[0] + ')' 

    def getListNodes(self):
        if(self.root != None):
            nodes = []
            self._getListNodes(self.root, nodes)
            return nodes
    
    def _getListNodes(self, node, nodes):
        if(node != None):
            nodes.append(node)
            self._getListNodes(node.l, nodes)
            self._getListNodes(node.r, nodes)