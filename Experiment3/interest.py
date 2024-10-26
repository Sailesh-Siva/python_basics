#Interest module

def simp_intr(p,n,r=11.5):
    return p*n*r/100
def comp_intr(p,n,r=11.5):
    A = p*(1 + (r/500))**(5*n) - p
    return A
