####### majority element n/2 times appears#########
a = [3, 3, 4, 2, 3, 3, 3]
n = len(a)

for i in range(n):
    count = 0
    for j in range(n):
        if a[i] == a[j]:
            count += 1
    if count > n // 2:
        print("Majority element is:", a[i])
        break
#####max sub array############
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(a)

max_current = max_global = a[0]

for i in range(1, n):
    # Choose the bigger between current element and current element + previous sum
    if a[i] + max_current > a[i]:
        max_current = a[i] + max_current
    else:
        max_current = a[i]
    
    # Update overall max
    if max_current > max_global:
        max_global = max_current

print("Maximum subarray sum is:", max_global)
