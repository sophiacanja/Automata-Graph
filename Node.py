from typing import List

class Node():  #node class is a subclass of graph class                #HELP: cannot complie, something wrong with inheritance

    def __init__(self, activity):         #sets trace and resources as a list
        self.activity = activity
        # self.resourceSet = resourceSet
        self.inputArcs = []
        self.outputArcs = []

#TODO: pass in resource set into the constructor of the resource class 

    def addInputArc(self, inputArc):
        self.inputArcs.append(inputArc)

    def addOutputArc(self, outputArc):
        self.outputArcs.append(outputArc)
    
    def getInputArcs(self):                     #maybe wont need this method
        return self.inputArcs

    def getOutputArcs(self):                    #maybe wont need this method
        return self.outputArcs
    
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