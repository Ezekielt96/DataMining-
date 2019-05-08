#Ezekiel D Towner
#Shortest longest Path Algorithm
#programming for data analysis

adjacencyList = {}

headNode = 0

inputFile = open("neighborList.csv",'r')
for line in inputFile :
        tokenizedLine = line.strip(). split(',')
        tmpList = []
        key =  -1
        for index,element in enumerate(tokenizedLine) :
                if index == 0 :
                        key = int(element)
                else :
                        tmpList.append(int(element))
        adjacencyList[key] = tmpList

inputFile.close()

weightList = {}

f = open("weightList.csv","r") #opens file with name of "test.txt"
for line  in f:
        weightedLine = line.strip(). split(',')
        myList = []
        key = -1
        for index2, element2 in enumerate(weightedLine):
                if index2 ==0:
                        key = int(element2)
                else:
                        myList.append (int(element))
        weightList[key] = myList
f.close()

        
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

def ShortestLongest (allPaths):
        pathCount = 0
        while allPaths != 0:
                for index in allPaths:
                        if len(index) > (pathCount-1):
                                count = len(index)
                                Path = index
                                print ("shortest Longest Path :" + str (Path))
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
        ShortestLongest(allPaths)

#correlate AdjacencyList with weightList 
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

print("")
print("All Possible Paths:")
print(allPaths)

topLength = 0
for path in allPaths :
	if len(path) > topLength :
		topLength = len(path)

filteredPath = []
for path in allPaths :
	if len(path) == topLength :
		filteredPath.append(path)
print ("")
print ("filtered Paths")
print ("")
print(filteredPath)


