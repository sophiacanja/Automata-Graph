import Node
import Arc
import numpy as np

class Graph: 
   
    def __init__(self, traces, resources):
        self.traceList = traces
        self.resourceList = resources
        self.nodeObjects = {}
        self.arcRelations = {}
        # self.inputs = []
        # self.outputs = []
        # self.data = data
        
        # relations: [A,B]

    def createIOnodesList(self):
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

        print("INPUT NODES LIST FOR ONE NODE")
        for node in self.nodeObjects:
            print("Node: " + node.activity)
            print("input nodes list: ")
            print(node.inputNodes)



    def buildGraph(self):                                                                   # creates nodes and arc relations by calling helper methods
        createNodes = self.createNodes()
        createArcs = self.createArcs()

    def createArcs(self):                                                                   # helper method that creates arc relations 
        print(self.traceList)
        print("CALLING CREATE ARCS METHOD")
        for currTrace in self.traceList:                                                    # forloop to traverse each trace in self.traceList
            print()
            print("Trace " + str(self.traceList.index(currTrace)+1))
            i = 0 
            j = 1 
            for currActivity in currTrace:                                                  # currTrace[i] will give you specific index of one trace
                # ex: [B, C, G]
                if (j < len(currTrace)):                                                     # checks if the loop is at the end of a trace
                    currActivityNode = self.nodeObjects.get(currTrace[i])                     
                    nextActivityNode = self.nodeObjects.get(currTrace[j])

                    # creates an arc relationship from two nodes
                    arcRelation = Arc.Arc(currActivityNode, nextActivityNode) 
                    print("arc: <" + arcRelation.relation + ">")
                    i += 1
                    j += 1

                    if (not(self.arcRelations.get(arcRelation.relation))):                   # puts non-duplicate arc nodes into dictionary
                        self.arcRelations[arcRelation.relation] = arcRelation               # key = string  ---- value = arcNode  EX: "BC" = <nodeB, nodeC> 
                    else: 
                        self.arcRelations.get(arcRelation.relation).addArcFrequency()       # if arcNode is duplicate, update arc frequency and add 1 
       

      # print(self.arcRelations.get('BC').outputNode.activity)   ---> this call allows you to get the val from dict and access outputNode of 'BC'(funct return is 'C')
                   
                
                
        
    def printArcList(self):                                                                 # prints the arcNodes in the dictionary
        print("CURRENT ARC LIST: ")         
        for arcs in self.arcRelations:
            print(arcs)
        

    def createNodes(self):                                                                  # helper method creates unique nodes 
        # generates an array of unique nodes from traces
        uniqueNodes = np.unique(np.array([elem for singleList in self.traceList for elem in singleList]))

        # creates node objects from array of unique nodes
        for nodeName in uniqueNodes:
            newNode = Node.Node(nodeName)
            self.nodeObjects[nodeName] = newNode            # new method: add nodeName and new object to nodeObjects dictionary
                                                            # ex: nodeObjects['A'] = nodeA
        return self.nodeObjects
   
    def printNodesList(self):
        print("CURRENT NODES LIST")
        for nodes in self.nodeObjects:  # printing out node objects
            print(nodes)

    def isValidTrace():
        return False

    def getTraceFrequency(trace):
        pass

myVar = Graph([["B","C","G"],["A","C","G"],["B","C","E","G"],["A","C","E","H"],["B","D","F","G"],["A","D","F","G"]],[{"R1":15,"R2":8,"R3":12,"R6":4,"R8":6,"R9":11,"R12":24,"R14":5,"R15":2},{"R2":10,"R5":24,"R6":3,"R7":12,"R9":4,"R11":22,"R14":8,},{"R3":2,"R6":12,"R12":1,"R15":36,},{"R1":12,"R6":3,"R9":1,},{"R1":2,"R2":1,"R3":1,"R8":1,"R9":2,"R11":6,"R14":1,"R15":2,},{"R4":1,"R6":1,"R8":2,"R13":1,}])


myVar.buildGraph()
myVar.createIOnodesList()
myVar.printArcList()
myVar.printNodesList()

# myVar.buildGraph()

# print("printing output nodes for B"  )
# print(myVar.nodeObjects.get("B").outputNodes)



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
