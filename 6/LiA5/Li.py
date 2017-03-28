import math

'''
Create by Dongning Li (Donnie)
SWE 5001 Software Engineering 1
Assignment 5
Create Date: Oct/02/2016

Eviroment: Mac Python 3

Function Define:
  readFile(filename)
  getMean(testArray) 
  getMedian(testArray) 
  getMode(testArray)
  getMinimum (testArray)
  getMaximum(testArray)
  getRange(testArray)
  getStandardDeviation(testArray)
  Main(filename)

Call main function to run whole program: Main(filename)
'''


'''
readFile(fileName)
Purpose: read the data from file and consist as an array
Limitation: First should be title. Beginning from 2nd line, should all be data. 5th line should be the close price
Return: the array consisted of close price as an array
'''
def readFile(fileName):
    dataFile = open(fileName, 'r')
    next(dataFile)
    
    testArray = []
    key = 0

    for aline in dataFile:
        items = aline.split(',')
        key += 1
        closePrice = float(items[4])
        testArray.append(closePrice)
    
    return testArray
    

def getMean(aList):
    return sum(aList) / len(aList)
    
    
def getMedian(aList):
    aList.sort()
    alistLength = len(aList)
    
    if (alistLength % 2) == 0:
        rightMid = alistLength // 2
        leftMid = rightMid -1
        medianNumber = (aList[rightMid] + aList[leftMid]) / 2
    else:
        mid = alistLength // 2
        medianNumber = aList[mid]
        
    return medianNumber
    

'''
getMode(aList)
Purpose: get the mode number of the arraylist
Limitation: each element in aList should be number and the length of aList should NOT 0.
Return: a set of mode number(s) if each elements in aList is number and the length of aList is NOT 0, else return ERROR.
'''     
def getMode(aList):
    countDict = {}
    for item in aList:
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
    
       
def getMinimum(aList):
    return min(aList)
    
    
'''
getMax(aList)
Purpose: get the max number of the arraylist
Limitation: each element in aList should be number and the length of aList should NOT 0.
Return: max number if each elements in aList is number and the length of aList is NOT 0, else return ERROR.
'''
def getMaximum(aList):
    return max(aList)
    
    
def getRange(aList):
    return max(aList) - min(aList)
    
    
def getStandardDeviation(aList): 
    theMean = getMean(aList)
    
    diffSum = 0
    for item in aList:
        diff = item - theMean
        diffsq = diff ** 2
        diffSum = diffSum + diffsq
        
    if (len(aList) - 1) == 0:
        sdev = 0
    else:
        sdev = math.sqrt(diffSum/(len(aList) - 1))
    
    return sdev
    
    
'''
getFrequencyTable(aList)
Purpose: Print the frequency table
Limitation: each element in aList should be number and the length of aList should NOT 0.
Print: Table consist of itemName and frequency
'''    
def getFrequencyTable(aList):
    print 'ITEM', '\t', 'FREQUENCY'
    sList = aList[:]
    sList.sort()
    
    coutList = []
    
    previous = sList[0]
    groupCount = 0
    
    for current in sList:
        if current == previous:
            groupCount = groupCount +1
            previous = current
        else:
            print previous, '\t', groupCount
            previous = current
            groupCount = 1
            
    print current,'\t', groupCount
    

'''
Summary(aList)
Purpose: Summary the statistic
Limitation: each element in aList should be number and the length of aList should NOT 0.
'''     
def Summary(testArray):
    print 'Array for test is: ', testArray
    
    '''
    if array is empty, print corresponding message
    if array contains NOT number, print corresponding message, then quit the system
    '''
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
        
        
def main(fileName):
    testArray = readFile(fileName)
    # testArray = [113.050003, 112.18, 113.949997, 113.089996, 112.879997, 112.709999, 114.620003, 113.550003, 113.57, 113.580002]
    Summary(testArray)
    
    
main('data.txt')