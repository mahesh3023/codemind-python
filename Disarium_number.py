n=int(input())
n=str(n)
c=0
for i in range(len(n)):
    c+=int(n[i])**(i+1)
print(c==int(n))