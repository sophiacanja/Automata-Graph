from typing import List

class Node():  #node class is a subclass of graph class                #HELP: cannot complie, something wrong with inheritance

    def __init__(self, activity):         #sets trace and resources as a list
        self.activity = activity
        # self.resourceSet = resourceSet
        self.inputNodes = []
        self.outputNodes = []

#TODO: pass in resource set into the constructor of the resource class 

    def addInputNode(self, inputNode):
        self.inputNodes.append(inputNode)

    def addOutputNode(self, outputNode):
        self.outputNodes.append(outputNode)
    
    def getInputNode(self):                     #maybe wont need this method
        return self.inputNodes

    def getOutputNode(self):                    #maybe wont need this method
        return self.outputNodes
    
    def getActivity(self):
        return self.activity

    def isInputArc(self, arc):
        for item in self.inputArcs:
            return arc == self.inputArcs[item]
        return False

    def isOutputArc(self, arc):
        for item in self.outputArcs:
            return arc == self.outputArcs[item]
        return False
    
    
# myVar = Node("a", ["amy", "marie"])
# myVar.addInputArc("t")
# print(myVar.isInputArc("z"))
# print(myVar.isInputArc("t"))