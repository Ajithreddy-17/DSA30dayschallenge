a = [1, 3, 5, 7, 9, 11]
target=7
n=len(a)
low=0
high=n-1
found=-1
while low <= high:
    mid = (low + high) //2
    if a[mid] == target:
        found = mid
        break
    elif a[mid] < target:
        low=mid+1
    elif a[mid] > target:
        high=mid-1
if found != -1:
    print("element found at index",found)
else:
    print("not found")

#########lower bound in binary search###########
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
print("lower bound is found at index",ans)

#########upper bound in binary search###########
a= [1, 3, 5, 7, 9, 11]
target=7
n=len(a)
low=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if a[mid] > target:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print("upper bound is found at index",ans)