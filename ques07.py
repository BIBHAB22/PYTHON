A=int(input("First side:"))
B=int(input("Second side:"))
C=int(input("Third side:"))
if(A==B==C):
    print("equilateral triangle")
elif(A==B!=C):
    print("scalene triangle")
else:
    print("isosceles triangle")