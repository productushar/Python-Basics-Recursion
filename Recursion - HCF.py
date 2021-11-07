#Recursion - HCF

def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(a,a%b)
