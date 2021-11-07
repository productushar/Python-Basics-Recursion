#Recursion - Reversing a number

def reverse(x, num=0):
    if x < 10:
        return num + x
    else:
        num = num * 10 + x%10 * 10
        return reverse(x // 10, num)
