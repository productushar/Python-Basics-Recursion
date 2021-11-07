#Recursion - Reversing the elements of an array

def reverses(s):
    l=len(s)
    if l==0:
        return s
    else:
        return reverses(s[1:])+s[0]
