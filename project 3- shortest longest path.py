# find all paths
# if the graph is a direct graph then, you have to use the recursive algorithm to find all paths
# do not use the iterative bfs or dfs to accumulate paths

adjacencyList = {}

headNodeId = 2
headNode = 0
inputFile = open("neighborList.csv",'r')
inputFile = open("weightList.csv",'r') 
for line in inputFile :
	tokenizedLine = line.strip().split(',')
	tmpList = []
	key =  -1
	for index,element in enumerate(tokenizedLine) :
		if index == 0 :
			key = int(element)
		else :
			tmpList.append(int(element))
	adjacencyList[key] = tmpList

inputFile.close()
visited = []
visited.append(headNode)

allPaths = []
def longestPath(allPaths): 
    pathCount = 0
    while allPaths != 0:
            for index in allPaths:
                    if len(index) > pathCount:
                            count = len(index)
                            Path = index
                            print("Longest Path: " + str(Path))
                            print ("")
                            return

def ShortestLongest (allPaths):
        pathCount = 0
        while allPaths != 0:
                for index in allPaths:
                        if len(index) > (pathCount):
                                count = len(index)
                                Path = index
                                print ("shortest Longest Path :" + str (Path))
                                print ("")
                                return
def recursiveDFS(parentNode) :

	# This is a leaf when all the elements have been visited
	visited.append(parentNode)
	

	# If this node does not have neighbors then we are 
	# at a leaf node, and we can append this path
	if parentNode.nodeId not in adjacencyList.keys() :
		
		allPaths.append(parentNode.path)
		return

	n_list = adjacencyList[parentNode.nodeId]
	visitedCount = 0
	# Remember newNode is an id, not of type Node
	for newNode in n_list :
		
		# If not in visited - getNode will return False
		vNode = getVisitedNode(newNode)
		if vNode == False :
			# Piggy back the path that was passed before us, and adding the child node
			newPath = parentNode.path.copy()
			newPath.append(newNode)
			# assign a color to this node based on the parent color
			node = Node(newColor,newPath,newNode)
			recursiveDFS(node)
		else :
			# check the visited node's color with the predicted color
			# if not a match then not a bi-partite graph

			# Increment the visit count
			visitedCount += 1
	if visitedCount == len(adjacencyList[parentNode.nodeId]) :
		allPaths.append(parentNode.path)
	return
# to accumulate paths in a graph - given anadjacencyList, weightList

# 1. create a class to hold the node info( paths, id, color)
class Node :
	# Constructor function, initializing an instance of Node
	def __init__(self,color,path,nodeId,weight) :
		# Creating the member value of color 
		self.color = color
		# Creating member path, this path already includes this node's id 
		self.path = path
		# Creating member nodeId
		self.nodeId = nodeId
		self.weight = weight
# 2. have a list of visited nodes

# 3. iterate over every element in the graph - headNode
    # we start off with color = 0
visited = []
allPaths = []

for headNodeId in adjacencyList.keys() :
	visited = []
	node = Node(0,[headNodeId],headNodeId,weight)
	visited.append(node)
	
	for n_node in adjacencyList[headNodeId] :
		if n_node in visited :
			continue
# 4. instantiation of the headNode(id, path, color, wieghts)
    # put this in the visitedList
# Iterate over the neighbors (neighborId) of headNode:
    # newPath = headNode.copy()
    # color = (headNode + 1) % numColors
    # newPath.append(neighborId)
for neighborId in adjacencyList[headNode] :
        if n_node in visited :
                continue
        newPath = [headNode]
        numColors = 2
        color = (headNode + 1) % numColors
        newPath.append(neighborId)
        node = Node(0, newPath, n_node, neighborId)
        wieghtPath = 0
        neighborNodeInst = Node(newPath, neighborId, wieghtPath, color)
        longestPath(allPaths)
        ShortestLongest(allPaths)

# 5. call the recursive fcn passing the instaniated neighborNode
    # this node is an instance of type Node, contains id, path, color
    # recursiveDFS(node)
        recursiveDFS(node)
        # note: make sure visitedList is a global variablefor key in adjacencyList :
#correlate AdjacencyList with weightList 
for key in adjacencyList:
        neighbors = adjacencyList[key]
        for index, element in enumerate(neighbors):
                print("For " + str(key)+ " To " + str(element)+ str(adjacencyList[key][index]))
    # 5a. Add the node to the visited list - visited list contains all your node instances that have been visited
    # 5b. check if its adjacencyList is empty, if it is empty we are at a leaf node
    #-- if we are adding up the paths e.g. longest path algorithm the append this path
    #allWeights.append(path)
    #-- allPaths.append(node, path)
    # 5c. iterate over the adjacencyList (childId) of node:
    #_________________True_________________________________
        # -- check if childId is in visitedList:
            # childNode is in visitedList
            # We know that this is a unique path and if we visited childId, then we will loop
            # create the calculated Id for childId -- (node.id + 1) % nColors
            # if calculatedId is not the same as childNode.id - it is not a n-partite graph
                #-- set the global variable isParrire to false
            #increment visitedCount
    #_______________________False________________________________
            # calculate the color from node
            #create a new path from node.path, and append childId is this newPath
            # instantiate the child node from the childId - newNode = Node(childId, newPath, color)
            # recursiveDFS(node)



    # 5.d check if our node only contains visited child links
    #_--if visitedCount = len(adjacencyList(node)) - number of child nodes
    #----------True------------------
    #-- we know we are at a leaf node
    # allPaths.append(node.path)
    # allWeights.append(node.weightPath)


pathMarker = -1
minCost = maxInt
#for index, weightList in allWeight:
#    add up all the weights in weightList
#    if this weight is less than minCost:
#        minCost = newWeight
#        pathMarker = index



print(allPaths)







            





            
