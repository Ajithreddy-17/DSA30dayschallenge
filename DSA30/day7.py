#### Two sum ############
a=[1,2,3,4,5,6]
target =10
n=len(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j]==target:
            print("at indices",i,j)
            print("numbers",a[i],a[j])
            found=1
            break

#########Sort an array of 0's 1's & 2's###########
a=[1,0,2,1,1,0,2,1,1,0]
n=len(a)
count0=count1=count2=0
for i in range(n):
    if a[i] == 0:
        count0+=1
    elif a[i] ==1:
        count1+=1
    else:
        count2+=1
j=0
for i in range(count0):
    a[j]=0
    j+=1
for i in range(count1):
    a[j]=1
    j+=1
for i in range(count2):
    a[j]=2
    j+=1
print("sorted array",a)
