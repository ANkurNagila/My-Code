from dis import dis
def add(x,y):
    return (lambda x,y: x+y)(x,y)   #Use of Lambda function

a,b=map(int,input().strip().split(" "))
print(add(a,b))
print("\n\n***********Assembly******************")
dis(add)
#print(dis(add))
p="Line Number"
q="Process going"
r="Functions/Elements"
print()
print(f"{p:<13}|{q:<16}|{r:>16}")
