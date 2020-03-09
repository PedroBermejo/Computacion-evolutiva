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
        self.nodes = []

    def getNodes(self):
        return self.nodes

    def createFromList(self, data):
        n = iter(data)
        self.root = Node(next(n))
        self.nodes.append(self.root)
        fringe = deque([self.root])
        while True:
            head = fringe.popleft()
            try:
                head.l = Node(next(n))
                fringe.append(head.l)
                self.nodes.append(head.l)
                head.r = Node(next(n))
                fringe.append(head.r)
                self.nodes.append(head.r)
            except StopIteration:
                break                

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root, self.root)
        else:
            return None

    def _find(self, val, node, parent):
        if(val is node):
            return parent
        else:
            if(node.l != None):
                return self._find(val, node.l, node)
            if(node.r != None):
                return self._find(val, node.r, node)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            print(str(node.v) + ' ')
            self._printTree(node.l)
            self._printTree(node.r)

    def getListNodes(self):
        if(self.root != None):
            nodes = []
            self._getListNodes(self.root, nodes)
            return nodes
    
    def _getListNodes(self, node, nodes):
        if(node != None):
            nodes.append(node)
            self._printTree(node.l)
            self._printTree(node.r)

    def printNodes(self):
        for node in self.nodes:
            print(node.v, end =" "),