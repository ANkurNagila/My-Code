line=input()
prev=None
count=0
for word in line:
    for element in word:
        try:
            if prev==element:
                count+=1
                break
        except:
            pass
            
        prev=element
        
print(count)
