####################### Rectangular Star Pattern ######################
n=5 
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
    
######################Pattern-2: Right-Angled Triangle Pattern #############
n=5 
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
################### Right-Angled Number Pyramid ################
n=5 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
################## Right-Angled Number Pyramid - II ##############
n=5 
for i in range(n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
################ Star Pyramid ###################
n=5 
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i*2+1):
        print('*',end="")
    print()
################### Diamond Star Pattern ###############
n=5 
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i*2+1):
        print('*',end="")
    print()
for i in range(n,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i*2+1):
        print('*',end="")
    print()
##################### Half Diamond Star Pattern #################  
n=5 
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(1,n):
    for j in range(n-i):
        print("*",end="")
    print()
################### Number Crown Pattern ######################
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(2*(n-i)):
        print(' ',end="")
    for m in range(i,0,-1):
        print(m,end="")
    print()
################## Increasing Number Triangle Pattern #################
num=1
n=5 
for i in range(n+1):
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()

#################### Increasing Letter Triangle Pattern ###################
n=5 
for i in range(n+1):
    for j in range(i+1):
        print(chr(65+j),end="")
    print()
####################### Symmetric-Void Pattern ###########################
n=5 
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    for k in range(i):
        print(' ',end=" ")
    for m in range(n-i):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    for k in range((n- i-1)*2):
        print(' ',end="")
    for m in range(i+1):
        print("*",end="")
    print()
########################Symmetric-Butterfly Pattern #####################
n = 6 
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    for k in range(2*(n-i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end="")
    for k in range(2*(n-i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
    
################### Hollow Rectangle Pattern #################

n = 6 
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end="")
        else:
            print(" ",end="")
    print()