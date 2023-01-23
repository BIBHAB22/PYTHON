n = chr(input("Enter the list size: "))
L = []
print("Enter the elements of the list: ")
count=0
for i in L:
    if(len(i)>count):
        count=len(i)
print(count)