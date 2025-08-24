########missing element in array#########
a=[1,2,4,5]
n=len(a)+1
sum=n*(n+1)//2
array_sum=0
for i in range(len(a)):
    array_sum += a[i]
sub = sum - array_sum
print("missing element is",sub)

#######max consecutive one#########
a=[1,1,0,1,1,1,0,1,1,1,1]
n=len(a)
count =0
max=0
for i in range(n):
    if a[i] == 1:
        count+=1
        if count>max:
            max=count
    else:
        count=0
print("maximum consecutive ones are",max)

#######find the number that appear ones#######
a=[1,1,2,3,2,4,4]
n=len(a)
for i in range(n):
    count=0
    for j in range(n):
        if a[i] == a[j]:
            count+=1
    if count == 1:
      print("the number that appears only once is",a[i])


