import random
import math

'''
Create by Dongning Li (Donnie)
SWE 5001 Software Engineering 1
Assignment 2
Sep/17/2016
'''

def euclidD(point1, point2):
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total = total + diff
        
    euclidDistance = math.sqrt(total)
    return euclidDistance
    
def readFile(filename):
        datafile = open(filename, "r")

        datadict = {}

        key = 0
        aline = datafile.readline()
        while aline !="":
                key = key + 1
                score = int(aline)
                datadict[key] = [score]

                aline = datafile.readline()
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
          
    
def main():
        datadict = readFile('cluster.txt')
        centroids = createCentroids(5, datadict)
        createClusters(5, centroids, datadict, 3)
main()