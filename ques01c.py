s1=input("Enter first string :")
s2=input("Enter second string :")
new_string=s1[0:int(len(s1)/2)]+s2+s1[int(len(s1)/2):]
print(new_string)