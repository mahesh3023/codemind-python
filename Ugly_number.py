def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if n<0:
    print("Not Ugly Number")
else:
    for i in range(7,n+1):
       if n%i==0 and prime(i):
          print("Not Ugly Number")
          break
    else:
        print("Ugly Number")