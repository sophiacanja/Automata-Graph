import Node,Arc

class Resources(Node, Arc): #resources is a subclass of both node and arc class

    def ___init__(self,resources):
        self.resources = {}     # ex: {"R1":2,"R3":4}
        
    def setResourceFreq(self):
        pass
        
    def getResourceFreq(self):
        pass
    
    def getResourceList(self, resources):
        return self.resources


myResource = Resources({'R1' : 2, 'R3' : 4})
 