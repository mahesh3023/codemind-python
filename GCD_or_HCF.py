l=list(map(int,input().split()))
for i in range(min(l[0],l[1]),0,-1):
    if l[0]%i==0 and l[1]%i==0:
        print(i)
        break