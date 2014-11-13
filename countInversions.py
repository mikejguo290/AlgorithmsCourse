
f = open('IntegerArray.txt', 'r')
integers = []
for line in f.readlines():
	integers.append(int(line))
#print integers[:100]
f.close()

print len(integers)

def CalcInversions(intList):
	# count the number of inversions at each step.  
	
	# base case comes first.
	if len(intList) ==1:
		return 0, intList 
	else:
	# divide step
		leftList,rightList = divideList(intList)
	
	# recursion step
		leftInv,sortedLeft = CalcInversions(leftList)
		rightInv,sortedRight = CalcInversions(rightList)
	# merge step, starting with the base case, all done by splitInv
		
		splitInv, mergedList = Merge_n_SplitInversions(sortedLeft,sortedRight)
	
	# n = 2, all split inversion, n>= 4, leftInv = n=2's split inverse, and so on.
		
	return leftInv + rightInv + splitInv, mergedList 
# i need to sort it using merge sort first!!! 

def divideList(intList):
	leftHalf= intList[0:int(len(intList)/2)]
	rightHalf= intList[int(len(intList)/2):]	
	return(leftHalf,rightHalf)
	
def Merge_n_SplitInversions(leftList,rightList):
	# Merge and count splitInversions. has to return a sorted list and number of inversions.
	mergedList = []
	splitInvCount = 0 
	n = len(leftList) + len(rightList) 
	i = 0
	j = 0
	k = 0
	while k < n :
		if i == len(leftList):
		# do stuff
			mergedList.extend(rightList[j:])
			break
		if j == len(rightList):
			mergedList.extend(leftList[i:])
			break
	
		if leftList[i]<=rightList[j]:
			# no inversion, so need for action
			mergedList.append(leftList[i])
			i +=1 # records how many have been appended to mergedList.
		else: 
			#elif rightList[j]<leftList[j]
			# the number of inversion is equal to the number of elements
			# 'left' in the left list.
			mergedList.append(rightList[j])
			splitInvCount += len(leftList) - i # indicates how many are left in leftList
			j +=1
		k+=1
	return  splitInvCount , mergedList


a, b = CalcInversions(integers)
print "the number of inversions are %s " % a
