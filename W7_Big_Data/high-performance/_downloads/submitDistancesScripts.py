#!/usr/bin/python
"""
Here we break a problem into 'chunks' and send the chunks to the cluster

The idea is that calculating all pairwise distance in a graph
can be done more efficiently by using multiple processors

We assume that the distances are symetrical so there aer 

    ((n*(n+1))/2) - n

total paths to find.
"""

import shutil,os,sys
import numpy as np
import networkx as nx

## ensure the queue directory present and clean
baseDir =  os.path.realpath(os.path.dirname(__file__))
queueDir = os.path.join(baseDir,'queue')
resultsDir = os.path.join(baseDir,'results')

for dirName in [queueDir,resultsDir]:
    if os.path.isdir(dirName):
        shutil.rmtree(dirName)
    os.mkdir(dirName)

## initialize the graph                                                               
G = nx.Graph(weighted=True)
n = 100

totDistances = ((n*(n+1))/2) - n
totDistancesAdded = 0
print "Graph size = %s, total pw distances = %s"%(n,totDistances)

for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        
        rn = np.random.randint(1,50)
        G.add_edge(str(i),str(j),weight=rn)
        totDistancesAdded +=1

## error checking
if len(G.nodes()) != n:
    raise Exception("G does not contain correct number of nodes (%s,%s)"%())
if totDistances != totDistancesAdded:
    raise Exception("Incorrect number of distances in G (%s,%s)"%(totDistances,totDistancesAdded))

## save the graph
nx.write_gpickle(G,os.path.join(baseDir,"network.pickle"))

## break the graph into chunks
chunks = 5
stopPoints = np.arange(0,totDistances,int(round(float(totDistances)/float(chunks))))
if stopPoints[-1] < totDistances:
    stopPoints = np.hstack([stopPoints[1:],np.array([totDistances])])

print '... submitting %s jobs'%(len(stopPoints))

begin = 0
for i,chunk in enumerate(range(stopPoints.size)):
    stop = stopPoints[chunk] 
    
    ## make a file for each chunk
    queueFileName = os.path.join(queueDir,"pwdist%s.sh"%i)
    queueLogName =  os.path.join(queueDir,"pwdist%s.log"%i)
    script = os.path.join(baseDir,"runDistances.py") + " -b %s -s %s"%(begin,stop)
    f = open(queueFileName, 'w')
    f.write("#!/bin/bash\n" + 
            "#$ -S /bin/bash\n" +
            "#$ -j yes\n" +
            "#S -M myemail@somewhere.com\n" +
            "#$ -o %s\n"%queueLogName + 
            "/usr/bin/python "+ script)

    f.close()

    ## submit the file to the cluster
    os.system("qsub " + queueFileName)
    begin = stop
