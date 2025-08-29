######### best time to buy and sell the  stock
a=[7, 1, 5, 3, 6, 4]
n=len(a)
min_price=a[0]
profit=0
for i in range(1,n):
    if a[i] <min_price:
        min_price=a[i]
    elif a[i]-min_price>profit:
        profit=a[i]-min_price
print(profit)

##### leaders in array ##########
a=[1,9,16,28,15,13,12,6]
n=len(a)
max=a[n-1]
print("leaders of the array",end=" ")
print(max,end=" ")
for i in range(n-2,-1,-1):
    if a[i] > max:
        max=a[i]
        print(max,end=" ")