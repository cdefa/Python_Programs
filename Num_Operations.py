"""
Purpose/Description: this program has three functions, take a certain input
and output a number or a list of numbers depending on each function
Author’s Panther ID: 6050200
Certification:
I hereby certify that this work is my own and none of it is the work of
any other person.
"""

 
"""
this function takes in a number (n) and add's all the even numbers
until that number
"""
def sum_even(n):

    if n == 0: 
        return 0
    
    elif n % 2 != 0: 
        n = n-1
        return n + sum_even(n-2)

    else :
        return n + sum_even(n-2)


"""
this function takes a list (L) and return the max number inside the list
by comparing each element with the next
"""

def get_max(L):

    if len(L)==1:
        return L[0]
    else:
        m = get_max(L[1:])
        return m if m > L[0] else L[0]


"""
this function takes a list (L) and a number (n) which represents the lenght
of the list and returns the min number of that list by comparing each element
with the next one
"""

def get_min1(L,n):
    if n == 0:
        return L[0]
    if len(L)==1:
        return L[0]
    else:
        m = get_min(L[1:n], n-1)
        return m if m < L[0] else L[0]





        
