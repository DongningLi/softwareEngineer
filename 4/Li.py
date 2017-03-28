'''
Create by Dongning Li (Donnie)
SWE 5001 Software Engineering 1
Assignment 2
09/19/2016
'''

def createClusters(k, centroids, datadict, repeats):
    
    # repeat getting centroid for "repeats" times
    apass = 0
    while apass < repeats:
        print("****PASS",apass,"****")
        clusters = []
        
        #create k clusters(empty kinds)
        i = 0
        while i < k:
           clusters.append([]) 
           i = i + 1            

        #get distance between different elements in dictionary
        akey = 1    
        while akey < len(datadict)+1:
            distances = []
            
            #for one cluster, cal each point distances to its corresponding centroid
            clusterIndex = 0
            while clusterIndex < k:
                dist = euclidD(datadict[akey],centroids[clusterIndex])
                distances.append(dist)
                clusterIndex = clusterIndex + 1
            
            #remeber the min distance from one element to k clusters
            # and then remember the index(which indicates the kth cluster)
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
            
            #replace centroid of cluster with corresponding sums
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