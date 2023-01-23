A=input("Enter a string :")
count1=0
count2=0
for i in A:
    if(i.isupper()):
        count1=count1+1
    elif(i.islower()):
        count2=count2+1
print(count1)
print(count2)