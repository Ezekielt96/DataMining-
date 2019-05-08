#Ezekiel D Towner
#Bi partite graph quiz 
#

import queue
import random


adjacencyList = {}

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


print(adjacencyList)
			
# We are going to use 0 as the head node, to insert onto the queue
myList = []   
myList.append(0)


color = 0
count = 0
visitedList = []
while len(myList) != 0 :
	# Popping the top element off of the list
	element = myList.pop(0)

    # Add element to the visited list
	visitedList.append(element)	

	# Iterate over the adjacencyList of element ( the neighbor nodes)
	for index,node in enumerate(adjacencyList[element]) :
		# These neighbor nodes should not be in the visited list or the list we are popping elements from
		if node not in visitedList and node not in myList :
			# Append the node to the queue
			myList.append(node)
			
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


# Print the order of visited nodes from left to right
print(visitedList)




