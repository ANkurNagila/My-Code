any=input("Enter anything to check for palindrome :")

pres=""
for i in any:
    pres=i+pres

if any == pres:
    print("Yes it a palindrome")
else:
    print("No it is not a palindrome")
