import matplotlib.pylab as plt
import sys
import csv
from pylab import *
a=input("Enter the width of slice ")
b=input("Enter the center of range ")
for j in range(1,len(sys.argv)):
	name="wsnapshot_"+sys.argv[j]+".csv"
	print("Plotting: "+name+" ...")
	f=open(name)
	r=csv.reader(f)
	d=list(r)
	i=0
	for i in range(1,262145):
		if(float(d[i][0])>b-(a/5) and float(d[i][0])<b+(a/5)):
			plt.plot([float(d[i][1])],[float(d[i][2])],markerfacecolor='blue', marker='o', markersize=1)

        plt.title("Y-Z plot")
        plt.grid(True)
        savefig('/home/vee8497/Downloads/Gadget-2.0.7/Project/Plots4/Y-Z Plot_'+sys.argv[j]+'.png',bbox_inches='tight')
        print("Done.")
        f.close()

