n1=int(input())
n2=int(input())
c1=0
c2=0
for i in range(1,n1):
    if n1%i==0:
        c1+=i
for i in range(1,n2):
    if n2%i==0:
        c2+=i
if n1==c2 and c1==n2:
    print("Amicable")
else:
    print("Not Amicable")