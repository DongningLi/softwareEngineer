import math

'''
Create by Dongning Li (Donnie)
SWE 5001 Software Engineering 1
Assignment 1
'''

def getMean(alist):
    return sum(alist) / len(alist)
    
    
def getMedian(alist):
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
    
    
def getMode(alist):
    
    countDict = {}
    for item in alist:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1

    countList = countDict.values()
    maxCount = max(countList)

    
    modeList = []
    for item in countDict:
        if countDict[item] == maxCount:
            modeList.append(item)
            
    return modeList
    
    
def getMinimum(alist):
    return min(alist)
    
    
def getMaximum(alist):
    return max(alist)
    
    
def getRange(alist):
    return max(alist) - min(alist)
    
    
def getStandardDeviation(alist): 
    theMean = getMean(alist)
    
    diffSum = 0
    for item in alist:
        diff = item - theMean
        diffsq = diff ** 2
        diffSum = diffSum + diffsq
        
    if (len(alist) - 1) == 0:
        sdev = 0
    else:
        sdev = math.sqrt(diffSum/(len(alist) - 1))
    
    return sdev
    
    
def getFrequencyTable(alist):
    print 'ITEM', '\t', 'FREQUENCY'
    slist = alist[:]
    slist.sort()
    
    coutList = []
    
    previous = slist[0]
    groupCount = 0
    
    for current in slist:
        if current == previous:
            groupCount = groupCount +1
            previous = current
        else:
            print previous, '\t', groupCount
            previous = current
            groupCount = 1
            
    print current,'\t', groupCount
    


# testArray = [2.9, 3.0, 2.5, 2.6, 3.2, 3.8]
# testArray = [5.40, 5.8, 5, 5.20, 5.40]
# testArray = [3, 3, 3, 3, 3]
# testArray = [17]
# testArray = []
# testArray = [4, 6, 5, 7, 8, 1, 9, 2, 50000]
# testArray = [-1, 0, 0, -2, 0, 43]
# testArray = [-0.3, -2, 3.2]
# testArray = [-3, -6, -3, -9, -10]
testArray = ['dog','cat', 0, -2]


print 'Array for test is: ', testArray
if testArray == []:
    print 'Array is empty'
else:
    for item in testArray:
        if(isinstance(item, (int, long, float, complex)) == 0):
            print 'This array contains something wired.'
            quit()
            
    theMean = getMean(testArray)
    theMedian = getMedian(testArray)
    theMode = getMode(testArray)
    theMinimum = getMinimum (testArray)
    theMaximum = getMaximum(testArray)
    theRange = getRange(testArray)
    theStandardDeviation = getStandardDeviation(testArray)

    print 'Mean is: ', theMean
    print 'Median is: ', theMedian
    print 'Mode is: ', theMode
    print 'Minimum is: ', theMinimum
    print 'Maximum is: ', theMaximum
    print 'Range is: ', theRange
    print 'Standard Deviation is: ', theStandardDeviation
    print 'Frequency Table is: '
    theFrequencyTable = getFrequencyTable(testArray)