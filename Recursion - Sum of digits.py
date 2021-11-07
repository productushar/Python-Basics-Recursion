#Recursion - Returning the sum of a number's digits

def sumdigi(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumdigi(n//10)
