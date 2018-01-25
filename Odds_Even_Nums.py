
"""
 Purpose/Description: This program takes two parameters p,q and use them to
 determine the lenght of two sets of evens and odds numbers and then prints
 pairs of numbers belong to this sets meeting some conditions
 Author’s Panther ID: 6050200
 Certification:
 I hereby certify that this work is my own and none of it is the work of
 any
"""
def myRelation(p,q):
    evens =[]
    odds =[]
    
    
    

    n = 1
    m = 2

    for x in range(n,p+1):
        odds.append(n)
        n+=2
    

    for x in range(m,q+2):
        evens.append(m)
        m+=2;
    

    print[(x,y) for x in odds  for y in evens if y%x==0 and x+y>p and x+y<q]
            
        
        


