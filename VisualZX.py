from pylab import *
import matplotlib.pyplot as plt
import sys
import csv
a=input("Enter the width of slice(float) ")
b=input("Enter the center of range(float) ")
for j in range(1,len(sys.argv)):

	name="wsnapshot_"+sys.argv[j]+".csv"
	print(name);
	f=open(name)
	r=csv.reader(f)
	d=list(r)
	i=0
	print("Plotting "+sys.argv[j]+"...")

	for i in range(1,262145):
		if(float(d[i][1])>(b-(a/2)) and float(d[i][1])<(b+(a/2))):
			plt.plot([float(d[i][2])],[float(d[i][0])],markerfacecolor='blue', marker='o', markersize=1)

	plt.title("Z-X plot")
	plt.grid(True)
	savefig('/home/vee8497/Downloads/Gadget-2.0.7/Project/Plots4/Z-X Plot_'+sys.argv[j]+'.png',bbox_inches='tight')
	print("Done.")
	f.close()

