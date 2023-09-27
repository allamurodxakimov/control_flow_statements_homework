def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    k=0
    l=0
    if a>0:
        k+=1
    if b>0:
        k+=1
    if c>0:
        k+=1
    if a<0:
        l+=1
    if b<0:
        l+=1
    if c<0:
        l+=1
    if k>l:
        return "there are a lot of positive numbers",k,l
    if k<l:
        return "there are a lot of negative numbers",k,l
   
print (main(2,-3,-4))