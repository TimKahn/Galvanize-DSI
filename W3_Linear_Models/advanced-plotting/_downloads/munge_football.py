#!/usr/bin/env python


import csv,sys

years = [1981,1983,1984,1985,1986,1988,1989,1990,1991,1992]
fidin = open("football.txt","r")
fidout =  open("football.csv","w")
reader = csv.reader(fidin,delimiter = " ")
writer = csv.writer(fidout)
header = reader.next()
writer.writerow(header+['season'])

count = 0
season = -1
last_week = 17
for linja in reader:
    linja = [l for l in linja if l != '']
    if len(linja) == 0:
        continue
    if len(linja) != len(header):
        raise Exception("bad line")
    
    current_week = int(linja[-1])

    if current_week < last_week:
        season +=1
        
    print count, linja, current_week, season

    writer.writerow(linja+[years[season]])
    
    count += 1
    last_week = current_week

fidin.close()
fidout.close()
print("done.")
