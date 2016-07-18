import sys
import csv
import math
from visual import *

InfoAddress=sys.argv[1]
info=open(IfoAddress,'rt')
info=info.read()
info=info.split('\n')
print(info[0])
	


print("Reading "+name+"...");
f=open(name)
r=csv.reader(f)
d=list(r)
max=0

name2="result_"+name
f2=open(name2,'wt')
w=csv.writer(f2)
w.writerow(('X','Y','Mass'))

grid=[[0 for x in range(0,101)] for y in range(0,101)]
for i in range(1,262145):
	posz=float(d[i][2])
	if(posz>=49 and posz<=51):
		posx=float(d[i][0])
		posy=float(d[i][1])
		x=int(math.floor(posx))
		y=int(math.floor(posy))
		grid[x][y]+=(x+1-posx)*(y+1-posy)
		grid[x+1][y]+=(posx-x)*(y+1-posy)
		grid[x][y+1]+=(x+1-posx)*(posy-y)
		grid[x+1][y+1]+=(posx-x)*(posy-y)
		if(grid[x][y] > max):
			max=grid[x][y]
		if(grid[x+1][y] > max):
                        max=grid[x+1][y]
		if(grid[x][y+1] > max):
                        max=grid[x][y+1]
		if(grid[x+1][y+1] > max):
                        max=grid[x+1][y+1]
	

bo=[]
for i in range(0,100):
	for j in range(0,100):
		bum=grid[i][j]/max
		if(bum>0.8):
			c=(bum,0,0)
		elif(bum>0.5):
			c=(1,1-(bum+0.10),0)
		elif(bum>0.25):
			c=(0,bum,0)
		else:
			c=(0,0,bum)
		bo.append(box(pos=(i-50,grid[i][j]/2,j-50),length=0.5, width=0.5, height=grid[i][j], color=c))
		w.writerow((i,j,grid[i][j]))
