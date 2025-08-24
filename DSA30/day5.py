######## move all zeros to end of an array########
a=[1,0,2,3,0,4,0,5,6]
n=len(a)
j=0
for i in range(n):
    if a[i] != 0:
        a[j] = a[i]
        j+=1
while j<n:
    a[j]=0
    j+=1
print(a)
#########linear search#######
a=[10,20,30,40,50,60]
key = 60
n=len(a)
found=0
for i in range(n):
    if a[i] == key:
        found = a[i]
if found == key:
    print("key element is found at index",i)
else:
    print("not found")

############ Binary Search in Python###################
a = [2, 4, 6, 8, 10, 12, 14, 16]  # Sorted array
n = len(a)
key = 10   # Element to search

low = 0
high = n - 1
found = -1   # will store index if found

while low <= high:
    mid = (low + high) // 2   # middle index

    if a[mid] == key:         # if key found
        found = mid
        break
    elif a[mid] < key:        # search right half
        low = mid + 1
    else:                     # search left half
        high = mid - 1

if found != -1:
    print("Element", key, "found at index", found)
else:
    print("Element", key, "not found")
