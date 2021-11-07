#Recursion - LCM

def lcm(a,b,i=1):
    if a==0 or b==0:
        return "Error"
    while i%a==0 and i%b==0:
        return i
    else:
        return lcm(a,b,i+1)
