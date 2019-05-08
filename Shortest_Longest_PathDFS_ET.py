#Ezekiel D Towner
#Longest Path Algorithm
#programming for data analysis

adjacencyList = {}

headNode = 0

inputFile = open("output.csv",'r') 
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


#print(adjacencyList)


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

def recursiveDFS(node,path) :
        # This is a leaf when all the elements have been visited
        visited.append(node)
        n_list = adjacencyList[node]
        for newNode in n_list :
                if newNode not in visited :
                        # Piggy back the path that was passed before us, and adding the child node
                        newPath = path.copy()
                        newPath.append(newNode)
                        recursiveDFS(newNode,newPath)           
        allPaths.append(path)   
#       print(" The path from 0 to " + str(node) + " is " + str(linkCount) )
#       linkCount -= 1
        return

for n_node in adjacencyList[headNode] :
        if n_node in visited :
                continue
        newPath = [headNode]
        newPath.append(n_node)
        recursiveDFS(n_node,newPath)
        longestPath(allPaths)


print(allPaths)

