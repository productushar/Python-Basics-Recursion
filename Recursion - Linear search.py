#Recursion - Linear search of an array

def linearsearch(lst,x,i=0):
    l=len(lst)
    if lst[i]==x:
        return i+1
    elif i==l-1:
        return "N/A"
    else:
        return linearsearch(lst,x,i+1)
