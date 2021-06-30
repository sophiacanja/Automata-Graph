
class Arc(): 

    def __init__(self, inputNode, outputNode): #took out resourceSet
        self.inputNode = inputNode
        self.outputNode = outputNode       
        self.relation = str(inputNode.activity) + str(outputNode.activity )     
        self.frequency = 1
       # self.resourceSet = resourceSet

#TODO: pass in resource set into the constructor of the resource class 

    def setInputNode(self, inputNode): 
        self.inputNode = inputNode

    def setOutputNode(self, outputNode):
        self.outputNode = outputNode

    def getInputNode(self):
        return self.inputNode

    def getOutputNode(self):
        return str(self.outputNode) 

    def addArcFrequency(self):
        self.frequency += 1

    def getArcFrequency(self):
        return self.frequency

    def getRelation(self):
        return self.relation

    
#myVar  = Arc(['a','b'] )
#myVar.setOutputNode('b')
#print("output node is" + myVar.getOutputNode())
#myVar.setArcFrequency(14)
#print("frequency set was " + "%s"%myVar.getArcFrequency())
        
