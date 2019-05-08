#Developer Ezekiel D Towner
# Apriori Algorithm
# Assignment 3
#Due 4/14/17


aprioriFile = open("tdb.txt","r") 
tdb = []

# Create the transaction database 
for line in aprioriFile :
	lineCharArray = line.strip('\n').split(',')
	lineArray = []
	for element in lineCharArray :
		lineArray.append(int(element))
	tdb.append(lineArray)
	
# This is our support variable
# n is the limiting number of transactions that our itemset appears in
n = 4

# K is our itemset length
k = 3

# F is our frequency map

print(tdb)
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
        
class F :

        def __init__(self) :
                # These are the list of itemsets that satisfy minimum support
                self.itemSet = []
                # A list of indices marking what transaction has the item
                self.itemIndices = []



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
F[0] = k_0
for element in frequencyMap :
	if frequencyMap[element] >= n :
		k_0.append([element])

#print(frequencyMap)

print(tdb)
print(F[0])
candidateSet = generateNext(F[0],F[0])
k = 0



#filter Alogorithm
for candidateItem in candidateSet:
        freqCount = 0
        #-For everyItemsets that satisfy minimum supporty 
        for transaction in tdb:
                if freqCount >= n :
                        F[k+1].append(candidateItem)

#Sequenced Apriori Algorithm
                        
while k < 3 :
        candidateSet = generateNext(F[k],F[0])
        for item in candidateSet:
                frequentCount = 0
                for transaction in tdb:
                        itemCount = 0
                        frequentCount +=1
                        if freqCount >= n:
                                F[k+1].append(item)
        F[k+1] = candidateSet
        print(" K " + str(k) + " candidateSet " + str(candidateSet))
        #check each subset and candidate set to see if it satifies minimum support
        k = k+1
        
#print(candidateSet)














