import numpy as np

class Graph: 
    nodeObjects = []

    def __init__(self, traces, resources):
        self.traces = traces
        self.resources = resources
        # self.inputs = []
        # self.outputs = []
        # self.data = data
        
        # relations: [A,B]

    def buildGraph(self): # calls createArcs and createNodes
        # root = Node("start", self.resources)
        # for trace in self.traces:
        #     for activity in trace:
                # create a node based on activity
        pass


    def createArcs(): # helper method
        pass

    def createNodes(self): # helper method
        uniqueNodes = np.unique(np.array([elem for singleList in self.traces for elem in singleList]))
        print(uniqueNodes)
        print(type(uniqueNodes))
        # for node in uniqueNodes:
        pass
            

    def isValidTrace():
        return False

    def getTraceFrequency(trace):
        pass

myVar = Graph([["B","C","G"],["A","C","G"],["B","C","E","G"],["A","C","E","H"],["B","D","F","G"],["A","D","F","G"]],[{"R1":15,"R2":8,"R3":12,"R6":4,"R8":6,"R9":11,"R12":24,"R14":5,"R15":2},{"R2":10,"R5":24,"R6":3,"R7":12,"R9":4,"R11":22,"R14":8,},{"R3":2,"R6":12,"R12":1,"R15":36,},{"R1":12,"R6":3,"R9":1,},{"R1":2,"R2":1,"R3":1,"R8":1,"R9":2,"R11":6,"R14":1,"R15":2,},{"R4":1,"R6":1,"R8":2,"R13":1,}])
myVar.createNodes()

# myVar.buildGraph()

# traces = [["B","C","G"],["A","C","G"],["B","C","E","G"],["A","C","E","H"],["B","D","F","G"],["A","D","F","G"]]
# resources = [{"R1":15,"R2":8,"R3":12,"R6":4,"R8":6,"R9":11,"R12":24,"R14":5,"R15":2},{"R2":10,"R5":24,"R6":3,"R7":12,"R9":4,"R11":22,"R14":8,},{"R3":2,"R6":12,"R12":1,"R15":36,},{"R1":12,"R6":3,"R9":1,},{"R1":2,"R2":1,"R3":1,"R8":1,"R9":2,"R11":6,"R14":1,"R15":2,},{"R4":1,"R6":1,"R8":2,"R13":1,}]

# graph = Graph("start")

# for trace in traces:
#     for activity in trace:
#         if activity.index() == 0:
#             graph.outputs


""" 
example input data from ryan's work

traces:    [["B","C","G"],["A","C","G"],["B","C","E","G"],["A","C","E","H"],["B","D","F","G"],["A","D","F","G"]]

resources: [{"R1":15,"R2":8,"R3":12,"R6":4,"R8":6,"R9":11,"R12":24,"R14":5,"R15":2},
            {"R2":10,"R5":24,"R6":3,"R7":12,"R9":4,"R11":22,"R14":8,},
            {"R3":2,"R6":12,"R12":1,"R15":36,},
            {"R1":12,"R6":3,"R9":1,},
            {"R1":2,"R2":1,"R3":1,"R8":1,"R9":2,"R11":6,"R14":1,"R15":2,},
            {"R4":1,"R6":1,"R8":2,"R13":1,}]
"""
