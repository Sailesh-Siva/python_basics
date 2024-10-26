#Functions Module
def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b,a%b)

def revNo(n):
    n = str(n)
    return(n[::-1])