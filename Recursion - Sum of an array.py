#Recursion - Returning the sum of an array's elements

def arraysum(l,i=0):
    if i==len(l):
        return 0
    else:
        return l[i]+(arraysum(l,i+1))
