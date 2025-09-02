#########count sub arrays sum equals k##########
a=[1,2,-3,2,1,1,2]
n=len(a)
count=0
k=3
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=a[j]
        if sum==k:
            count+=1
print(count)

######### check palindrome##########
s="madam"
n=len(s)
is_palindrome=True
for i in range(n//2):
    if s[i]!=s[n-i-1]:
        is_palindrome=False
        break
if is_palindrome:
    print("palindrome")
else:
    print("not palindrome")

####largest odd digit##########
s="4209"
n=len(s)
index=-1
for i in range(n-1,-1,-1):
    if int(s[i]) % 2==1:
        index=i
        break
if index==-1:
    print("")
else:
    print(s[:index+1])