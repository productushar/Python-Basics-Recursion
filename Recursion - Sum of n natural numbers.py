#Recursion - sum of n natural numbers

def sumn(x):
    if x==0:
        return x
    else:
        return x+sumn(x-1)
