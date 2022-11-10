#lab06.py
from Apartment import Apartment

def mergesort(apartmentList):
	if len(apartmentList) > 1:
		mid = len(apartmentList) // 2
			
		lefthalf = apartmentList[:mid]
		righthalf = apartmentList[mid:]
			
		mergesort(lefthalf)
		mergesort(righthalf)
			
		i = 0 
		j = 0
		k = 0
			
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				apartmentList[k] = lefthalf[i]
				i = i + 1
			else:
				apartmentList[k] = righthalf[j]
				j = j + 1
			k = k + 1
				
		while i < len(lefthalf):
			apartmentList[k] = lefthalf[i]
			i = i + 1
			k = k + 1
				
		while j < len(righthalf):
			apartmentList[k] = righthalf[j]
			j = j + 1
			k = k + 1
	return apartmentList

def ensureSortedAscending(apartmentList):
	for i in range(len(apartmentList) - 1):
		if apartmentList[i] > apartmentList[i+1]:
			return False
	return True

def getBestApartment(apartmentList):
	sortedList = mergesort(apartmentList)
	return sortedList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
	sortedList = mergesort(apartmentList)
	return sortedList[-1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
	best = mergesort(apartmentList)
	returnstring = ""
	for i in range(len(best)):
		if best[i].getRent() < budget or best[i].getRent() == budget:
			returnstring += best[i].getApartmentDetails() + "\n"
	return returnstring[:-1]


