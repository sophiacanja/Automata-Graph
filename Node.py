from typing import List


class Node: 

    def __init__(self, trace, resourceSet):         #sets trace and resources as a list
        self.trace = []
        self.resourceSet = []
        self.outputArc = []
        self.inputArc = []


    def setInputArc(self, inputArc):
        pass

    def setOutputArc(self, outputArc):
        pass
    
    def getInputArc(self, inputArc):
        pass

    def getOutputArc(self, outputArc):
        pass
    
#myVar = Node(["a", "b"], ["amy", "marie"])