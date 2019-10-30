import random

array1 = [1,5,10,2,11,16,3,12,17,100,99,98,97,96,95,50]
array2 = [] # 100 -> 1
array3 = [] # 10 entries
array4 = [] # 100 entries
array5 = [] # 1000 entries
array6 = [] # 10000 entries
n = 100
count = 0

# Filling each array
for x in range(0,n):
	array2.append(x+1)

for x in range(0,10):
	array3.append(random.randint(1,100))

for x in range(0,100):
	array4.append(random.randint(1,100))
	
for x in range(0,1000):
	array5.append(random.randint(1,100))
	
for x in range(0,10000):
	array6.append(random.randint(1,100))
	
# Reverse the array
array2 = array2[::-1]

def pickPivot(a,l,h):
	r = (l-1)
	p = a[h]
	holder = 0
	for x in range(l,h):
		if a[x] <= p:
			r+=1
			holder = a[r]
			a[r] = a[x]
			a[x] = holder
	holder = a[r+1]
	a[r+1] = a[h]
	a[h] = holder
	return (r+1)

def quickSort(a,l,h):
	if l < h:
		pivot = pickPivot(a,l,h)
		# Recursive calls for quickSort
		quickSort(a,l,pivot-1)
		quickSort(a,pivot+1,h)
	print(a)


quickSort(array1,0,len(array1)-1)
#quickSort(array2,0,len(array2)-1)
quickSort(array3,0,len(array3)-1)
#quickSort(array4,0,len(array4)-1)
#quickSort(array5,0,len(array5)-1)
#quickSort(array6,0,len(array6)-1)


#def pickPivot(array, count):
#	low = array[0]
#	mid = array[int(len(array)/2)]
#	high = array[len(array)-1]
#	holder = 0
#	print(array)
#	
#	if (low > mid and low < high) or (low > high and low < mid):
#		holder = array[len(array)-1]
#		array[len(array)-1] = array[0]
#		array[0] = holder
#		pickPivot(array[0:int(len(array)/2)],count)
#	elif (mid > low and mid < high) or (mid > high or mid < low):
#		holder = array[len(array)-1]
#		array[len(array)-1] = array[int(len(array)/2)]
#		array[int(len(array)/2)] = holder
#		pickPivot(array[int(len(array)/2):len(array)-1],count)
#	elif (high > low and high < mid) or (high > mid and high < low):
#		pickPivot(array[int(len(array)/2):len(array)-1],count)
#	print(low)
#	print(high)
#	print(mid)
#	print(array)

#quickSort(array,2,5)