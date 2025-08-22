########largest element in array########
a=[10,29,33,22,11,9,77]
largest=a[0]
n=len(a)
for i in range(n):
    if a[i] > largest:
        largest = a[i]
print(largest)

########secound largest element###########
a = [10, 29, 33, 11, 9, 77]
largest = a[0]
second_largest = float('-inf')  
n = len(a)

# Find the largest
for i in range(n):
    if a[i] > largest:
        largest = a[i]

# Find the second largest
for j in range(n):
    if a[j] != largest and a[j] > second_largest:
        second_largest = a[j]

print(second_largest,"secound largest")


#####sorting#############
a=[19,22,33,11,10,44,24]
n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if (a[j] > a[j+1]):
            a[j],a[j+1] = a[j+1],a[j] #swap
print(a,"sorted array")
print(a[0],"smallest element")
print(a[n-1],"largest element")


###check the array is sorted or not##############
a=[1,2,3,4,599]
flag = True
n=len(a)
for i in range(n-1):
    if a[i] > a[i+1]:
        flag = False
if flag:
    print("sorted")
else:
    print("not sorted")

##########secound smallest element##########
a=[10,4,11,15,9,29]
smallest=a[0]
secound_smallest=float('inf')
n=len(a)
for i in range(n):
    if a[i] < smallest:
        smallest =a[i]
for j in range(n):
    if (a[j] != smallest and a[j] < secound_smallest):
        secound_smallest = a[j]
print(secound_smallest)

