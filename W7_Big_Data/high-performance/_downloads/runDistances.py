#!/usr/bin/python


import os,sys,getopt,csv
import networkx as nx

### process inputs   
if len(sys.argv) < 2:
    print sys.argv[0] + " -b (begin) -s (stop)"
    raise Exception("Incorrect number of args")
try:
    optlist, args = getopt.getopt(sys.argv[1:], 'b:s:')
except getopt.GetoptError:
    print sys.argv[0] + "-b (begin) -s (stop)"
    sys.exit()

begin,stop = None,None
for o, a in optlist:
    if o == '-b':
        begin = int(a)
    if o == '-s':
        stop = int(a)

## load the network
baseDir =  os.path.join("..",os.path.realpath(os.path.dirname(__file__)))
resultsDir = os.path.join(baseDir,'results')
G = nx.read_gpickle(os.path.join(baseDir,"network.pickle"))

## create a results file
outFile = os.path.join(resultsDir,"out-%s-%s.csv"%(begin,stop))
outFid = open(outFile,'w')
writer = csv.writer(outFid)
writer.writerow(["i","j","distance"])

pathsToFind = range(begin,stop)
n = len(G.nodes())
count = -1
for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        count += 1
        if count in pathsToFind:
            length,path=nx.bidirectional_dijkstra(G,str(i),str(j))
            writer.writerow([i,j,length])

outFid.close()
