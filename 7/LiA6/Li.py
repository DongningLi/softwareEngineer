from scipy import stats


'''
Create by Dongning Li (Donnie)
Course Name: SWE 5001 Software Engineering 1
Assignment Number: Assignment 6
Create Date: Oct/22/2016
'''


def checkIfEmptyList(aList):
    listLength = len(aList)
    
    if (listLength == 0):
        return True
    else:
        return False


def getSortedList(aList):
    
    #sort list from lowest to highest
    aList.sort()
    
    return aList


def getTrimmedList(aList, alpha):
    listLength = len(aList)
    
    '''
    if length of list  * alpha is NOT an integer
    forcely keep round off it
    then convert result to integer type to use as index of list 
    '''
    listIndex = int(round(listLength * alpha))
    
    return aList [listIndex : listLength-listIndex]
    
    
def getListMean(aList):
    listLength = len(aList)
    
    '''
    in case that mean is a decimal
    forcely convert summary into float type before getting mean
    '''
    listSumF = float(sum(aList))
    
    return listSumF / listLength


def getTrimmedMean(aList, alpha):
    sortedList = getSortedList(aList)
    trimmedList = getTrimmedList(sortedList , alpha)
    
    if(len(trimmedList) == 0):
        return None
    else:
        listMean = getListMean(trimmedList)
        return listMean
    
    
def main(aList, alpha):
    
    ifEmpty = checkIfEmptyList(aList)
    if (ifEmpty):
        print ("List is empty.")
    else:
        for item in aList:
            if(isinstance(item, (int, long, float, complex)) == 0):
                print 'This list contains something wired.'
                quit()
        trimmedMean = getTrimmedMean(aList, alpha)
        if (trimmedMean == None):
            print "Every elements have been trimmed."
        else:
            print "The trimmed mean is: ", trimmedMean
    
  
main([0,0,0,0,0], 0.2)
main([-5, 5, 20, 5, 5], 0.2)
main([], 0.6)
main([-10, 5, 3.2, -2.4, -100, 7004], 0.2)
main([-10, 5, 3.2, -2.4, -100, 7004], 0.6)
main([-9, 0, -30.2, 7, 100, 86.9], 0.45)
# main([-9, 7, 'why', 'what'], 0.45)