from pylab import *
import matplotlib.pyplot as plt
import sys
import csv
a=input("Enter the width of slice ")
b=input("Enter the center of range ")
for j in range(1,len(sys.argv)):

	name="wsnapshot_"+sys.argv[j]+".csv"
	print(name);
	f=open(name)
	r=csv.reader(f)
	d=list(r)
	i=0
	print("Plotting "+sys.argv[j]+"...")

	for i in range(1,262145):
		if(float(d[i][2])>b-(a/5) and float(d[i][2])<b+(a/5)):
			plt.plot([float(d[i][0])],[float(d[i][1])],markerfacecolor='blue', marker='o', markersize=1)

	plt.title("X-Y plot")
	plt.grid(True)
	savefig('/home/vee8497/Downloads/Gadget-2.0.7/Project/Plots4/X-Y Plot_'+sys.argv[j]+'.png',bbox_inches='tight')
	print("Done.")
	f.close()

