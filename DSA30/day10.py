#########Longest Consecutive Sequence in an Array######
a=[100,1,2,104,3,105,4]
n=len(a)
for i in range(n):
    for j in range(0,n-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
longest=1
current=1
for i in range(n):
    if a[i] == a[i-1]+1:
        current+=1
    elif a[i] != a[i-1]:
        if current>longest:
            longest=current
        current=1
print("Longest Consecutive Sequence is",longest)

#########next permutation#########
a = [1, 2, 3]
n = len(a)

# Step 1: Find pivot
i = n - 2
while i >= 0 and a[i] >= a[i + 1]:
    i -= 1

if i == -1:
    # reverse entire array manually
    left, right = 0, n-1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
else:
    # Step 2: Find just larger than pivot
    j = n - 1
    while a[j] <= a[i]:
        j -= 1

    # Step 3: Swap
    a[i], a[j] = a[j], a[i]

    # Step 4: Reverse right side
    left, right = i + 1, n - 1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

# Result
print("Next permutation:", end=" ")
for num in a:
    print(num, end=" ")




