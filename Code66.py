from random import choice
import string
from tabulate import tabulate
from operator import itemgetter

devices=list()
T=int(input("Enter the number of devices you want:"))
for i in range(T):
    device=dict()

    device["Name"]=choice(["r1","r3","r4","r6","r10"])
    device["Vendor"]=choice(["cisco","wipro","arista","juniper"])

    if device["Vendor"]=="cisco":
        device["OS"]=choice(["ios","linux","nexus"])
        device["version"]=choice(["1.0","2.0","3.0"])

    elif device["Vendor"]=="wipro":
        device["OS"]=choice(["Windows","kali","garunda"])
        device["version"]=choice(["12.0","2.0","31.0"])

    elif device["Vendor"]=="arista":
        device["OS"]=choice(["debian","linux","nexus"])
        device["version"]=choice(["11.0","2.10","3.01"])

    elif device["Vendor"]=="juniper":
        device["OS"]=choice(["ios","linux","nexus"])
        device["version"]=choice(["1.20","23.0","13.0"])

    device["IP"]="10.0.0"+str(i)
    devices.append(device)


print("\n-------- Devices as Sorted List of Table------------\n")
Sort_list=sorted(devices,key=itemgetter("Vendor","OS","version"))
print(tabulate(Sort_list,headers="keys"))
