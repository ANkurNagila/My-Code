from pprint import pprint

Service=int(input("Enter number of devices: "))
Devices={}
Device={}
for Serial in range(1,Service+1):
    Name=input("Enter the Name of device:")
    IP=input("Enter Mac address:")
    Type=input("Enter Device type:")

    Device={"Name":Name,"IP":IP,"Type":Type}

    Devices[Serial]=Device

print("\t\t-------------Simple Print------------------")
print(Devices,"\n\n\n")

print("\t\t-------------Preety Print------------------")
pprint(Devices)
print("\n\n")

print("\t\t-------------Format Print-------------------")
for i,j in Devices.items():
    print("Serial Number",i,":")
    for x,y in j.items():
        print(f"{x:>16}:{y}")
    print("\n\n")
