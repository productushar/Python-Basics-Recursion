#Recursion - Checking whether a number is prime or not

def palindrome(x,num=0,y=0):
    def reverse(x,num=0,y=y):
        if x < 10:
            return num+x
        else:
            num=num * 10 + x%10 * 10
            return reverse(x // 10, num)
    if reverse(x)==x:
        return True
    else:
        return False
      
