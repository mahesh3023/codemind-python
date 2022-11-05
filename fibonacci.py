n=int(input())
if n==1:
    print(0)
elif n==2:
    print(0,1)
else:
    print(0,1,end=' ')
    x=0
    y=1
    i=2
    while(i<n):
        z=x+y
        x=y
        y=z
        print(z,end=' ')
        i+=1