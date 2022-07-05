class Graph:
    def __init__(self):
        self.data = dict()
        self.nextData = list()

    def addElement(self, newData):
        if self.data is None:
            self.nextData = addElement(newData)
        else:
            self.data = newData

    def removeElement(self, newData):
        pass

    def searchElement(self, newData):
        pass

    def sizeGraph(self):
        pass

    def quantWaysGraph(self):
        pass


graph = Graph()

# creating our graph:
graph.addElement(1)
graph.addElement(2)
graph.addElement(3)
graph.addElement(4)

"""
# Other Example:
# Create the dictionary with graph elements
graph = { "a" : ["b","c"],
                 "b" : ["a", "d"],
                 "c" : ["a", "d"],
                  "d" : ["e"],
                  "e" : ["d"]
         }
 
# Print the graph          
print(graph)
"""
