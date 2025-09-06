#########first occurrence and last occurrence##########
a = [1, 2, 2, 2, 3, 4, 5]
x=2
n=len(a)
low=0
high=n-1
first=-1
####first ocurrence
while low <= high:
    mid =(low+high)//2
    if a[mid]==x:
        first=mid
        high=mid-1
    elif a[mid] < x:
        low=mid+1
    else:
        high=mid-1
print("first occurrence",first)
######last occurence
low=0
high=n-1
last=-1
while low <= high:
    mid=(low+high)//2
    if a[mid]==x:
        last=mid
        low=mid+1
    elif a[mid] < x:
        high=mid-1
    else:
        low=mid+1
print("last occurrence is",last)
        