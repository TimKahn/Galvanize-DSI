#!/usr/bin/env python
"""
simple example to show how to handle arguments
"""

import sys,getopt

## collect args
argString = "%s -f filepath -d [optional debug]"%sys.argv[0]
try:
    optlist, args = getopt.getopt(sys.argv[1:],'f:d')
except getopt.GetoptError:
    print getopt.GetoptError
    raise Exception(argString)

## handle args
debug = False
filePath = None
for o, a in optlist:
    if o == '-f':
        filePath = a
    if o == '-d':
        debug = True

if filePath == None:
    raise Exception(argString)
if not os.path.exists(filePath):
    print("... %s"%filePath)
    raise Exception("bad file path")
                    
