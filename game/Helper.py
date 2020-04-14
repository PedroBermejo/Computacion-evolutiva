import random
import math
import operator


class helper:

    # Calculates number of all nodes in a tree given depth
    def calculateNumberOfNodes(depth):
        numbNodes = 0
        for i in range(depth):
            numbNodes = numbNodes + math.pow(2, i)
        return numbNodes
