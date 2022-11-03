n=int(input())
if (n**2)%(10**(len(str(n))))==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")