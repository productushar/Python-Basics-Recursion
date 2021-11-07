#Recursion - Multiplication Table

def multiplicationtable(x,num=1):
    if num==11:
        return 0
    else:
        print(x,"*",num,"=",x*num)
        multiplicationtable(x,num+1)
