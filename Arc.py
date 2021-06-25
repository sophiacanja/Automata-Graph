import Graph

class Arc(Graph): 

    def __init__(self, relation, resourceSet):
        self.relation = relation              #ex: <A,B>
        self.inputNode = relation[0]
        self.outputNode = relation[1]
        self.frequency = 0
        self.resourceSet = resourceSet

#TODO: pass in resource set into the constructor of the resource class 

    def setInputNode(self, inputNode):
        self.inputNode = inputNode

    def setOutputNode(self, outputNode):
        self.outputNode = outputNode

    def getInputNode(self):
        return self.inputNode

    def getOutputNode(self):
        return self.outputNode 

    def setArcFrequency(self, frequency):
        self.frequency = frequency

    def getArcFrequency(self):
        return self.frequency

    
#myVar  = Arc(['a','b'] )
#myVar.setOutputNode('b')
#print("output node is" + myVar.getOutputNode())
#myVar.setArcFrequency(14)
#print("frequency set was " + "%s"%myVar.getArcFrequency())
        
