from typing import List
import Graph


class Node(Graph):  #node class is a subclass of graph class

    def __init__(self, activity, resourceSet):         #sets trace and resources as a list
        self.activity = activity
        self.resourceSet = resourceSet
        self.inputArcs = []
        self.outputArcs = []

#TODO: pass in resource set into the constructor of the resource class 


    def setInputArc(self, inputArc):
        pass

    def setOutputArc(self, outputArc):
        pass
    
    def getInputArcs(self):
        return self.inputArcs

    def getOutputArcs(self):
        return self.outputArcs
    
    def getActivity(self):
        return self.activity
    
    
#myVar = Node(["a", "b"], ["amy", "marie"])