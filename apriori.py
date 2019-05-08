

aprioriFile = open("tdb.txt","r") 

tdb = []
user_input_2 = input("enter your n value ")
# Create the transaction database 
for line in aprioriFile :
	lineCharArray = line.strip('\n').split(',')
	lineArray = []
	for element in lineCharArray :
		lineArray.append(int(element))
	
	tdb.append(lineArray)
	
# This is our support variable
# n is the limiting number of transactions that our itemset appears in
n = int(user_input_2)

# K is our itemset length
k = 1

# F is our frequency map

#print(tdb)
def hasDuplicate(ourNext,c) :
	# a = [ [ ], [ ], [ ] ]
    # b = [ ]
    # The subset length in a is the same length as b

	foundDuplicate = False
	for subset in ourNext :
		count = 0
		for element in c :
			if element in subset :
				count += 1
		if count == len(subset) :
			foundDuplicate = True
			break

	return foundDuplicate


# HERE a is our F[K] and b is our F[0] where elements in F[0] are not in F[k] 
def generateNext(a,b) :
    # a = [ [] , [], []  ]
    # b = [ [1], [2], [3], .. ]   b contains single element subsets
	ourNext  = []
	#  For each element in b:
    #  make a copy of a, 
    #  iterate over a, making copies of the elements in a (a-copy)
    #  append the b element into the a-copy only if b is not in a-copy

	# IF you are find F[k+1]
    # check if this subset meets the minimum support before you 
    # add this to the F[k+1] list

		
	for item in b :
		aCopy = a.copy()
		# ----------- a  -----  x --  b -------  = append  append  append
        # [ [1] , [2 ], [3]  ]  x  [ [5] ] -->   [ [1,5], [2,5], [3,5] ] 
		c = []
		for aElement in aCopy :
			c = aElement.copy()
			if item[0] not in c :
				c.append(item[0])
				if hasDuplicate(ourNext,c) == False :
					ourNext.append(c)

	return ourNext
		
			

# CREATE F[0]
frequencyMap = {}
for transactions in tdb :
	for element in transactions :
		if element in frequencyMap.keys() :
			# HERE WE ARE INCREMENT THE COUNT FOR THE ITEM 
			frequencyMap[element] += 1 
		else :
			# HERE WE ARE CREATING THE MAP 
			frequencyMap[element] = 1


F = {}
k_0 = []
F[k] = k_0
for element in frequencyMap :
	if frequencyMap[element] >= n :
		k_0.append([element])

print(frequencyMap)

while k != 0:
        print(F[k])
        
        candidateSet = generateNext(F[k],F[k])
        print(candidateSet)
        k = k -1







