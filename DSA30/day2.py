#countdigit
n=7789782
count=0
while(n>0):
    last_digit=n%10
    count +=1
    n=n//10
print(count)

#revrse a number
n=7789
reverse=0
while(n>0):
    last_digit=n%10
    n=n//10 
    reverse=(reverse*10)+last_digit
print(reverse)

#check palindrome
n=1331
dup=n
reverse=0
while(n>0):
    last_digit = n%10
    n = n//10
    reverse = (reverse*10)+last_digit
if dup == reverse:
    print("palindrome number")
else:
    print("not a palindrome")

#armstrong number
n=371
dup=n
sum=0
while(n>0):
    last_digit = n%10
    n=n//10
    sum=sum+(last_digit*last_digit*last_digit)
if sum == dup:
    print("armstorng number")
else:
    print("not a armstrong number")

#divisors
n=36
for i in range(1,n+1):
    if (n%i == 0):
        print(i)

#gcd or hcf
a=9
b=12
gcd=0
for i in range(1,min(a,b)+1):
    if(a%i==0 and b%i==0):
        gcd=i
print(gcd)

#prime number
n=17
count=0
for i in range(1,11+1):
    if (n % i==0):
        count +=1
if count > 2:
    print("not a prime")
else:
    print("prime number")

a=52
b=10
while(a>0 and b>0):
    if (a>b):
        a=a%b
    else:
        b=b%a
if a==0:
    print(b)
else:
    print(a)
