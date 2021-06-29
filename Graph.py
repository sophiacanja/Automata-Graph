import Node
import Arc
import numpy as np

class Graph: 
   
    def __init__(self, traces, resources):
        self.traceList = traces
        self.resourceList = resources
        self.nodeObjects = {}
        self.arcRelations = []
        # self.inputs = []
        # self.outputs = []
        # self.data = data
        
        # relations: [A,B]

    def buildGraph(self):
        for currTrace in self.traceList:
            print("Trace " + str(self.traceList.index(currTrace)+1))
            prev = 0
            nxt = 2
            for currActivity in currTrace:
               # print(currActivity)
                if len(currTrace) > 1:  # check if trace has more than 1 activity
                    
                    # example trace [B, C, G]
                    # case 1: first activity in trace
                    if currTrace.index(currActivity) == 0:
                        # activity name of the output node; ex: "C"
                        outputActivity = currTrace[1]

                        # the output node, is added to the list of output nodes ex: nodeC
                        outputNode = self.nodeObjects.get(outputActivity)
                        currNode = self.nodeObjects.get(currActivity)
                        currNode.addOutputNode(outputNode)
                        print("Current node is " + currNode.getActivity() + " (first)")
                        print("output node: " + outputNode.getActivity())
                   

                    # case 2: last activity in trace
                    elif currTrace.index(currActivity) == len(currTrace)-1:
                        inputActivity = currTrace[len(currTrace)-2]
                        inputNode = self.nodeObjects.get(inputActivity)
                        currNode = self.nodeObjects.get(currActivity)
                        currNode.addInputNode(inputNode)
                        print("Current node is " + currNode.getActivity() + " (last)")
                        print("input node: " + inputNode.getActivity())
                        
                    # case 3: remaining activities in trace
                    else:
                        inputActivity = currTrace[prev]
                        inputNode = self.nodeObjects.get(inputActivity)
                        
                        outputActivity = currTrace[nxt]
                        outputNode = self.nodeObjects.get(outputActivity)

                        currNode = self.nodeObjects.get(currActivity)
                        currNode.addInputNode(inputNode)
                        currNode.addOutputNode(outputNode)

                        prev += 1
                        nxt += 1
                        print("Current node is " + currNode.getActivity())
                        print("input node: " + inputNode.getActivity())
                        print("output node: " + outputNode.getActivity())
                print("----------------------")
            print()



        
    def createArcs(self): # helper method           #TODO: make arcRelations[] 
        print(self.traceList)
        for currTrace in self.traceList:               #forloop to traverse each trace in self.traceList
            print("Trace " + str(self.traceList.index(currTrace)+1))
            i = 0 
            j = 1 
            for currActivity in currTrace:              #currTrace[i] will give you specific index of one trace
                # ex: [B, C, G]
                if(j < len(currTrace)):
                    currActivityNode = self.nodeObjects.get(currTrace[i])
                    nextActivityNode = self.nodeObjects.get(currTrace[j])
                    arcRelation = Arc.Arc(currActivityNode, nextActivityNode) 
                    print("arc: <" + arcRelation.getInputNode().activity + "," + arcRelation.getOutputNode().activity + ">")
                    i += 1
                    j += 1
                    
                
                
        
        
        

    def createNodes(self): # helper method
        uniqueNodes = np.unique(np.array([elem for singleList in self.traceList for elem in singleList]))
        for nodeName in uniqueNodes:
            newNode = Node.Node(nodeName)
            # old method: add to new object to nodeObjects list
            # self.nodeObjects.append(newNode)

            # new method: add nodeName and new object to nodeObjects dictionary
            # ex: nodeObjects['A'] = nodeA
            self.nodeObjects[nodeName] = newNode
       
        # for i in self.nodeObjects:  #printing out node objects
        #      print(i.activity)
        # print("COMPLETED")
        return self.nodeObjects
   

    def isValidTrace():
        return False

    def getTraceFrequency(trace):
        pass

myVar = Graph([["B","C","G"],["A","C","G"],["B","C","E","G"],["A","C","E","H"],["B","D","F","G"],["A","D","F","G"]],[{"R1":15,"R2":8,"R3":12,"R6":4,"R8":6,"R9":11,"R12":24,"R14":5,"R15":2},{"R2":10,"R5":24,"R6":3,"R7":12,"R9":4,"R11":22,"R14":8,},{"R3":2,"R6":12,"R12":1,"R15":36,},{"R1":12,"R6":3,"R9":1,},{"R1":2,"R2":1,"R3":1,"R8":1,"R9":2,"R11":6,"R14":1,"R15":2,},{"R4":1,"R6":1,"R8":2,"R13":1,}])

myVar.createNodes()
myVar.createArcs()

myVar.buildGraph()

#print("printing output nodes for B"  )
#print(myVar.nodeObjects.get("B").outputNodes)



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
