s1=input("Enter first string :")
s2=input("Enter second string :")
new_string=s1[0]+s1[int(len(s1)//2)]+s1[-1]+s2[0]+s2[int(len(s2)//2)]+s2[-1]
print(new_string)