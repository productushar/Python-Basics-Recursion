#Recursion - Checking whether a number is prime or not

def prime(n,i=1,x=0):
    if n<2 and n>=0:
        return "Error Value"
    while i<=n:
        if n%i==0:
            x+=1
        if i!=n:
            return prime(n,i+1,x=x)
        elif i==n:
            if x==2:
                return True
            elif x>2:
                return False
