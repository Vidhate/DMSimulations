import sys
import csv
import math
import numpy as np
from visual import *

name="ICread_set1_1.csv"
print("Reading "+name+"...");
f=open(name)
r=csv.reader(f)
d=list(r)
max=0

name2="3Dresult_"+name
f2=open(name2,'wt')
w=csv.writer(f2)
w.writerow(('X','Y','Z','Mass'))

grid=np.zeros((101,101,3))

for i in range(1,262145):
	posz=float(d[i][2])
	if(posz>=49 and posz<=51):
		posx=float(d[i][0])
		posy=float(d[i][1])
		
		x=int(math.floor(posx))
		y=int(math.floor(posy))
		z=int(math.floor(posz))-49

		grid[x,y,z]+=(x+1-posx)*(y+1-posy)*(z+1-posz+49.0)
		grid[x+1,y,z]+=(posx-x)*(y+1-posy)*(z+1-posz+49.0)
		grid[x,y+1,z]+=(x+1-posx)*(posy-y)*(z+1-posz+49.0)
		grid[x,y,z+1]+=(x+1-posx)*(y+1-posy)*(posz-z-49.0)
		grid[x+1,y+1,z]+=(posx-x)*(posy-y)*(z+1-posz+49.0)
		grid[x,y+1,z+1]+=(x+1-posx)*(posy-y)*(posz-z-49.0)
		grid[x+1,y,z+1]+=(posx-x)*(y+1-posy)*(posz-z-49.0)
		grid[x+1,y+1,z+1]+=(posx-x)*(posy-y)*(posz-z-49.0)
		
		if(grid[x,y,z]>max):
			max=grid[x,y,z]
		elif(grid[x+1,y,z]>max):
                        max=grid[x+1,y,z]
		elif(grid[x,y+1,z]>max):
                        max=grid[x,y+1,z]
		elif(grid[x,y,z+1]>max):
                        max=grid[x,y,z+1]
		elif(grid[x+1,y+1,z]>max):
                        max=grid[x+1,y+1,z]
		elif(grid[x,y+1,z+1]>max):
                        max=grid[x,y+1,z+1]
		elif(grid[x+1,y,z+1]>max):
                        max=grid[x+1,y,z+1]
		elif(grid[x+1,y+1,z+1]>max):
                        max=grid[x+1,y+1,z+1]


bo=[]
for k in range(0,3):
	for i in range(0,100):
		for j in range(0,100):	
			if(i%2==0 and j%2==0):
				bum=(grid[i,j,k]+grid[i+1,j,k]+grid[i+1,j+1,k]+grid[i,j+1,k])/(max*4)
				if(bum>0.8):
					c=(bum,0,0)
				elif(bum>0.5):
					c=(1,1-(bum+0.10),0)
				elif(bum>0.25):
					c=(0,bum,0)
				else:
					c=(0,0,bum)
				bo.append(sphere(pos=(i-50,k*5,j-50),radius=bum, color=c))
			w.writerow((i,j,k+49,grid[i,j,k]))
