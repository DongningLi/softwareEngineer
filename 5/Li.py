import random
import math
import turtle

'''
Create by Dongning Li (Donnie)
SWE 5001 Software Engineering 1
Assignment 3
Sep/23/2016
'''

def euclidD(point1, point2):
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total = total + diff
        
    euclidDistance = math.sqrt(total)
    return euclidDistance
    
def readFile(filename):
    datafile = open(filename, 'r')
    next(datafile)
    
    datadict = {}
    key = 0

    for aline in datafile:
        items = aline.split(',')
        key += 1
        lat = float(items[1])
        lon = float(items[2])
        datadict[key] = [lon,lat]
    
    return datadict

def createCentroids(k, datadict):
        centroids=[]
        centroidCount = 0
        centroidKeys = []

        while centroidCount < k:
                rkey = random.randint(1,len(datadict))
                if rkey not in centroidKeys:
                        centroids.append(datadict[rkey])
                        centroidKeys.append(rkey)
                        centroidCount = centroidCount + 1
        return centroids

def createClusters(k, centroids, datadict, repeats):
    
    # repeat getting centroid for "repeats" times
    apass = 0
    while apass < repeats:
        print("****PASS",apass,"****")
        clusters = []
        
        #create k clusters
        i = 0
        while i < k:
           clusters.append([]) 
           i = i + 1            

        #get distance between different elements in dictionary
        akey = 1    
        while akey < len(datadict)+1:
            distances = []
            
            #cal distances to different clusters
            clusterIndex = 0
            while clusterIndex < k:
                dist = euclidD(datadict[akey],centroids[clusterIndex])
                distances.append(dist)
                clusterIndex = clusterIndex + 1
            
            #remeber the min distance from one element to k clusters
            #and then remember the index(which indicates the kth cluster)
            mindist = min(distances)
            index = distances.index(mindist)
            
            # put the value into the min-distance-cluster
            clusters[index].append(akey)
            
            akey = akey + 1 
        
        dimensions = len(datadict[1])  
                
        #calculate new centroid and replace the old one
        
        clusterIndex = 0
        while clusterIndex < k:

            sums = [0]*dimensions
        
            #sum all value in one cluster
            akeyi = 0
            while akeyi < len(clusters[clusterIndex]):
                
                akey = clusters[clusterIndex][akeyi]
                datapoints = datadict[akey]
                
                ind = 0
                while ind < len(datapoints):
                    sums[ind] = sums[ind] + datapoints[ind]
                    ind = ind + 1
                    
                akeyi = akeyi + 1
                
            #calculate average of all value in one cluster
            ind = 0
            while ind < len(sums):
                
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind]/clusterLen
                    
                ind = ind + 1
            
            #replace centroid of cluster with sum
            centroids[clusterIndex] = sums
            
            clusterIndex = clusterIndex + 1
            
        # print
        c = 0
        while c < len(clusters):
            print ("CLUSTER")
            keyi = 0
            while keyi < len(clusters[c]):
                key = clusters[c][keyi]
                print(datadict[key], end=" ")
                keyi = keyi + 1

            print ()
            c = c + 1 
            
        apass = apass + 1
            
    return clusters
    
def visualizeQuakes(filename):
    
    datadict = readFile(filename)
    quakeCentroids = createCentroids(6, datadict)
    clusters = createClusters(6, quakeCentroids, datadict, 7)
    
    #create a litlle cute turtle
    quakeT = turtle.Turtle()
    #create a screen
    quakeWin = turtle.Screen()
    #load the map file as an background image
    quakeWin.bgpic("worldmap.gif") 
    #set the size of screen
    #set the size of screen
    quakeWin.screensize(800,600)  
    
    '''
    calculate a factor elment
    when used, by multipling this factor, 
    modify latitude from [-90, 90] to [0, 448]
    and longtitude from [-180, 180] to [0,266]
    '''
    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90
    
    quakeT.hideturtle()
    quakeT.up()
    
    # distribute different colof to different cluster
    colorlist = ["red","green","blue","orange","cyan","yellow"]  

    #draw lines and points
    for clusterIndex in range(6):
        quakeT.color(colorlist[clusterIndex])  
        for akey in clusters[clusterIndex]:
            
            #get the first element of each pair of keys
            #where first one is longtitude
            lon = datadict[akey][0]
            lat = datadict[akey][1]
            #draw lines within the range
            quakeT.goto(lon*wFactor,lat*hFactor)
            #draw points
            quakeT.dot()
            
    #exit and close screen when click        
    quakeWin.exitonclick()
    
def main():
    visualizeQuakes('4.5_month.csv')
    
main()