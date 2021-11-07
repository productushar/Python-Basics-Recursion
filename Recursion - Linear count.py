#Recursion - Linear count

def linearcount(lst,x,i=0,j=0):
    l=len(lst)
    if lst[i]==x:
        return linearcount(lst,x,i+1,j+1)     
    elif i==l-1:
        return j
    else:
        return linearcount(lst,x,i+1,j)  
