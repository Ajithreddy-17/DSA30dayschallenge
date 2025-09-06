
#########floor and ceil in binary search##########
a = [1, 3, 5, 7, 9, 11]
x = 6
n = len(a)

# Floor
low = 0
high = n - 1
floor_val = -1

while low <= high:
    mid = (low + high) // 2
    if a[mid] == x:
        floor_val = a[mid]
        break
    elif a[mid] < x:
        floor_val = a[mid]   # candidate for floor
        low = mid + 1
    else:
        high = mid - 1

# Ceil
low = 0
high = n - 1
ceil_val = -1

while low <= high:
    mid = (low + high) // 2
    if a[mid] == x:
        ceil_val = a[mid]
        break
    elif a[mid] > x:
        ceil_val = a[mid]   # candidate for ceil
        high = mid - 1
    else:
        low = mid + 1

print("Floor:", floor_val)
print("Ceil:", ceil_val)

##########search and insert##############
a= [1, 3, 5, 7, 9, 11]
n=len(a)
target=7
low=0
high=n-1
ans=n
while low<=high:
    mid=(low+high)//2
    if a[mid] >= target:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print("insert at index",ans)