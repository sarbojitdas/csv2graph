#loading a data from file and represent on graph
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
##from pandas import ExcelWriter
##from pandas import ExcelFile
#import xlrd
def file_loading(f):
    with open(f,'r') as csvfile:
        readCSV=csv.reader(csvfile, delimiter=',')
##        for row in readCSV:
##            print(row)
        x,y=np.loadtxt(csvfile,delimiter=',',unpack=True)
        plt.plot(x,y,label='loaded from file')
        plt.xlabel('student number')
        plt.ylabel('student growth')
        plt.title('general graph')
        plt.legend()
        plt.show()













file=input("enter the name of the file=")


file_loading(file)


##
##
##file=input("enter the file name")
##print(file_loading(file))
