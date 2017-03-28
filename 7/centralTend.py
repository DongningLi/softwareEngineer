from scipy import stats

'''
Create by Dongning Li (Donnie)
SWE 5001 Software Engineering 1
Assignment 6
10/30/2016
'''

def mean(alist):
    return sum(alist) / len(alist)

    
def median(alist):
    alist.sort()
    alistLength = len(alist)
    
    if (alistLength % 2) == 0:
        rightMid = alistLength // 2
        leftMid = rightMid -1
        medianNumber = (alist[rightMid] + alist[leftMid]) / 2
    else:
        mid = alistLength // 2
        medianNumber = alist[mid]
        
    return medianNumber


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


def trimmedMean(aList, alpha):
    sortedList = getSortedList(aList)
    trimmedList = getTrimmedList(sortedList , alpha)
    
    if(len(trimmedList) == 0):
        return None
    else:
        listMean = getListMean(trimmedList)
        return listMean
        
        
def centralTend(aList, alpha):
    
    ifEmpty = checkIfEmptyList(aList)
    if (ifEmpty):
        print ("List is empty.\n")
    else:
        for item in aList:
            if(isinstance(item, (int, long, float, complex)) == 0):
                print 'This list contains something wired.\n'
                quit()
                
        meanList = mean(aList)
        medianList = median(aList)
        trimmedMeanList = trimmedMean(aList, alpha)
        
        print "The mean is: ", meanList
        print "The median is: ", medianList
        if (trimmedMean == None):
            print "Every elements have been trimmed.\n"
        else:
            print "The trimmed mean is: ", trimmedMeanList, "\n"
            
            
centralTend([0,0,0,0,0], 0.2)
centralTend([-5, 5, 20, 5, 5], 0.2)
centralTend([], 0.6)
centralTend([-10, 5, 3.2, -2.4, -100, 7004], 0.2)
centralTend([-10, 5, 3.2, -2.4, -100, 7004], 0.6)
centralTend([-9, 0, -30.2, 7, 100, 86.9], 0.45)
centralTend([-9, 7, 'why', 'what'], 0.45)            