import sys
import csv
import math
import numpy as np
import matplotlib as plt


for j in range(1,len(sys.argv)):
	name=sys.argv[j]+".csv"
	print("Reading "+name+"...");
	f=open(name)
	r=csv.reader(f)
	d=list(r)
	
	name2="Power_sepc"+sys.argv[j]+".csv"
	f2=open(name2,'wt')
	f2=csv.writer(f2)
	f2.writerow(('k','Power'))

	rho=np.zeros((101,101,101))

	for i in range(1,262144):
		posx=float(d[i][0])
		posy=float(d[i][1])
		posz=float(d[i][2])	

		x=int(math.floor(posx))
		y=int(math.floor(posy))
		z=int(math.floor(posz))


		rho[x,y,z]+=(x+1-posx)*(y+1-posy)*(z+1-posz)
		rho[x+1,y,z]+=(posx-x)*(y+1-posy)*(z+1-posz)
		rho[x,y+1,z]+=(x+1-posx)*(posy-y)*(z+1-posz)
		rho[x,y,z+1]+=(x+1-posx)*(y+1-posy)*(posz-z)
		rho[x+1,y+1,z]+=(posx-x)*(posy-y)*(z+1-posz)
		rho[x,y+1,z+1]+=(x+1-posx)*(posy-y)*(posz-z)
		rho[x+1,y,z+1]+=(posx-x)*(y+1-posy)*(posz-z)
		rho[x+1,y+1,z+1]+=(posx-x)*(posy-y)*(posz-z)
	
	c=262144.00/(10**6)							# In Mass units per Mpc cube
	for i in range(0,100):
		for j in range(0,100):
			for k in range(0,100):
				rho[i,j,k]=(rho[i,j,k]/c)-1
	
	ftpert=np.fft.rfftn(rho)
	
	kmin=(2*3.14)/100
	kmax=(2*3.14)
	
	rhoInBin=0.0
	nInBin=0

	Power=np.zeros((100))
	for i in range(0,99):
		lowBin=kmin+(i*(kmax-kmin)/50)
		highBin=lowBin+((kmax-kmin)/50)
		for l in range(0,100):
			for m in range(0,100):
				for n in range(0,100):
					if l!=0 and m!=0 and n!=0:
						modK=math.sqrt((2*3.14)**2 / ((1.0/l**2) + (1.0/m**2) + (1.0/n**2)))
						if modK >= lowBin and modK < highBin:
							rhoInBin+=(ftpert[l,m,n].conjugate() * ftpert[l,m,n])
						nInBin+=1
						
		Power[i]=rhoInBin/nInBin
		
	plt.plot(np.arange(kmin,kmax,1,100),Power,markerfacecolor='blue', marker='o', markersize=1)
	plt.show()
	plt.title('Power Spectrum')
	savefig('/home/vee8497/Downloads/MuSIC Cosmology/Project/set4/Power Spectrum.png',bbox_inches='tight')

	
		
	
	f.close()
