#######removing duplicates from sorted array#########
a=[11,22,33,33,44,44,55,55]
n=len(a)
j=0
for i in range(1,n):
    if a[j] != a[i]:
        j+=1
        a[j] = a[i]
for i in range(j+1):
    print(a[i],end=" ")
print()

###########removing duplicates in unsorted array#########
a=[99,55,99,11,22,44,55,11]
n=len(a)
unique=[0]*n
j=0
for i in range(n):
    for k in range(j):
        if a[i] == unique[k]:
            break
    else:
        unique[j] = a[i]
        j+=1
for i in range(j):
    print(unique[i],end=" ")
print()

#########left rotate array by one plac######
a=[10,20,30,40,50]
n=len(a)
temp=a[0]
for i in range(1,n):
    a[i-1] = a[i]
a[n-1] = temp
print(a,"after left rotating an array")


#####left rotate by array by D places#########
a=[10,20,30,40,50,55,60]
n=len(a)
d=3
temp=[0]*d
for i in range(d): # Step 1: Store first d elements
    temp[i] = a[i]
for i in range(d,n): # Step 2: Shift remaining elements to the left
    a[i-d] = a[i]
for i in range(d): # Step 3: Copy stored elements at the end
    a[n-d+i] = temp[i]
print(a)