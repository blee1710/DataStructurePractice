# Implementation of an undirected graph
class Graph:
    def __init__(self):
        self.nodeCount = 0
        self.adjList = {}
    
    def addVertex(self, node):
        if node not in self.adjList:
            self.adjList[node] = []
            self.nodeCount += 1 
            return self 
        else:
            return False
    
    def addEdge(self, node1, node2):
         if node1 in self.adjList and node2 in self.adjList:
             if self.adjList[node1].count(node2) == 0:
                 self.adjList[node1].append(node2)
             if self.adjList[node2].count(node1) == 0:
                 self.adjList[node2].append(node1)
             return self 
         else:
             return False
    
    def showConnections(self):
        for node in self.adjList:
            connections = ''
            for connection in self.adjList[node]:
                connections += str(connection) + " "
            print('{} ----> {}'.format(node, connections))

myGraph = Graph()

myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('2') # repeated adding
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1') 
myGraph.addEdge('3', '1') # repeated adding
myGraph.addEdge('3', '4') 
myGraph.addEdge('4', '2') 
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2') 
myGraph.addEdge('1', '0') 
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')

myGraph.showConnections()

# Expected output: 
# 0 ----> 1 2 
# 1 ----> 3 2 0 
# 2 ----> 4 1 0 
# 3 ----> 1 4 
# 4 ----> 3 2 5 
# 5 ----> 4 6 
# 6 ----> 5