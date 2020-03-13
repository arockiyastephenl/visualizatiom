import tkinter as tk
#import requests
import pandas as pd
import numpy as np
import scipy as sp
import time
import matplotlib.pylab as plt
from matplotlib import style
#import tkinter
import tkinter.messagebox
style.use('ggplot')
#%matplotlib inline
#print(time.ctime())
#csv file opening
HEIGHT=300
WIDTH=200
def helloCallBack():
    table=pd.read_csv('sampledata.csv',delimiter=',',engine='python')
    print(table)
    data=pd.read_csv('sampledata.csv',usecols = ['Production real'])
    data1=pd.read_csv('sampledata.csv',usecols = ['Machine'])
    eff=pd.read_csv('sampledata.csv',usecols = ['OEF'])
    work=pd.read_csv('sampledata.csv',usecols = ['Work Time'])
    ukg=pd.read_csv('sampledata.csv',usecols = ['UKG'])
    legend=['Production real','Avg count','OEF']

    #Bar chart with Production real

    plt.figure(figsize=(10, 10))
    plt.bar(x = np.arange(1,17),height = table['Production real'],color=['blue'],align='center',width=0.5)
    plt.title("Machine Performance",fontsize=24)
    plt.xticks(np.arange(1,17),table['Machine'],rotation=90)

    #Bar chart with Avg count

    plt.bar(x = np.arange(1,17),height = table['Avg count'],color=['orange'],align='center',width=0.5)
    plt.xticks(np.arange(1,17),table['Machine'],rotation=90)

    #Bar chart with OEF

    plt.bar(x = np.arange(1,17),height = table['OEF'],color=['green'],align='center',width=0.5)
    plt.xticks(np.arange(1,17),table['Machine'],rotation=90)
    plt.legend(legend,loc='upper right', frameon=False)
    plt.xlabel("Machine",fontsize=20)
    plt.ylabel("Efficiency",fontsize=20)
    #plt.show()

    #Performance Calculation
    q=0
    y=1
    for i in data:
        li=data[i]
        l=(list(li))
        l.sort(reverse=True)
    #print(l)
    for i in data1:
        lj=data1[i]
        v=(list(lj))
    #print(v)
    p=len(data)
    print('Production Based Performance')
    print('\n')
    print('\t\tTop 5 High performance Machines')
    for i in range(5):
        for j in range(p):
            if l[i] == li[j]:
                k=j
                print("\t\t\t\t\tMachine no",y,"---->",v[k])
                y+=1
    for i in data:
        li=data[i]
        l=(list(li))
        l.sort()
    #print(l)
    '''for i in data1:
        lj=data1[i]
        v=(list(lj))
    #print(v)'''
    p=len(data)
    y=1
    print('\t\tTop 5 Low performance Machines')
    for i in range(5):
        for j in range(p):
            if l[i] == li[j]:
                k=j
                print("\t\t\t\t\tMachine no",y,"---->",v[k])
                y+=1
    for i in eff:
        li=eff[i]
        l=(list(li))
        l.sort(reverse=True)
    p=len(eff)
    y=1;
    print('\n')
    print('Efficiency Based Performance')
    print('\n')
    print('\t\tTop 7 High Efficiency Machines')
    for i in range(5):
        for j in range(p):
            if l[i] == li[j]:
                k=j
                print("\t\t\t\t\tMachine no",y,"---->",v[k])
                y+=1
    for i in eff:
        li=eff[i]
        l=(list(li))
        l.sort()
    p=len(eff)
    y=1
    print('\t\tTop 5 Low Efficiency Machines')
    for i in range(5):
        for j in range(p):
            if l[i] == li[j]:
                k=j
                print("\t\t\t\t\tMachine no",y,"---->",v[k])
                y+=1
    print('\n')
    Mac = table["Machine"]
    Time = table["Work Time"]
    plt.figure(figsize=(10, 10))
    plt.plot(Mac,Time)
    plt.title("Machine Working Time",fontsize=24)
    plt.xlabel('Machine',fontsize=18)
    plt.ylabel('Working Time(Min)',fontsize=18)
    #plt.show()
    print('\n')
    for i in work:
        li=work[i]
        l=(list(li))
        l.sort(reverse=True)
    p=len(work)
    y=1;
    print('\n')
    print('Working Time Based Performance')
    print('\n')
    print('\t\tTop 5 High Working time Machines')
    for i in range(5):
        for j in range(p):
            if l[i] == li[j]:
                k=j
                print("\t\t\t\t\tMachine no",y,"---->",v[k])
                y+=1
    for i in work:
        li=work[i]
        l=(list(li))
        l.sort()
    p=len(work)
    y=1
    print('\t\tTop 5 Low Working time Machines')
    for i in range(5):
        for j in range(p):
            if l[i] == li[j]:
                k=j
                print("\t\t\t\t\tMachine no",y,"---->",v[k])
                y+=1
    x = table["Machine"]
    y = table["UKG"]
    plt.figure(figsize=(10, 10))
    plt.scatter(x,y)
    plt.title("Unit Consumed by Every Machine ",fontsize=24)
    plt.xlabel('Machine',fontsize=18)
    plt.ylabel('Unit Consumed(KG)',fontsize=18)
    #plt.show()
    for i in ukg:
        li=ukg[i]
        l=(list(li))
        l.sort()
    p=len(ukg)
    y=1;
    print('\n')
    print('Unit consumed Based Performance')
    print('\n')
    print('\t\tTop 5 Low Power consumed Machines')
    for i in range(5):
        for j in range(p):
            if l[i] == li[j]:
                k=j
                print("\t\t\t\t\tMachine no",y,"---->",v[k])
                y+=1
    for i in ukg:
        li=ukg[i]
        l=(list(li))
        l.sort(reverse=True)
    p=len(ukg)
    y=1
    print('\t\tTop 5 High Power consumed Machines')
    for i in range(5):
        for j in range(p):
            if l[i] == li[j]:
                k=j
                print("\t\t\t\t\tMachine no",y,"---->",v[k])
                y+=1
    time.sleep(5)
    plt.show()
    
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='Coats.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root)
frame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.2)

label=tk.Label(frame,text="Madura Coats Pvt Limited",bg="lightgreen",font=40)
label.place(relx=0.25,rely=0.2,relheight=0.4, relwidth=0.5)

button = tk.Button(frame, text="Click", font=40, bg="lightblue",command=helloCallBack)
#button.place(relx=0.35, relheight=0.1, relwidth=0.3)
button.pack(side='bottom')


#lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
#lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#label = tk.Label(lower_frame)
#label.place(relwidth=1, relheight=1)

root.mainloop()
