import math
from fractions import Fraction #fractions library used for better accuracy
#Greedy algorithm for finding Egyptian fractions
def egyptian(f):
    result = []  
    numerator = f[0]
    denominator = f[1]
        
    while numerator > 0:  
        unit_fraction = math.ceil(Fraction(denominator , numerator))
        result.append(unit_fraction)  
        
        numerator = numerator * unit_fraction - denominator
        denominator = denominator * unit_fraction
    return result
    
def egyptian_no_library(f): #Doesn't use fractions library
    result = []  
    numerator = f[0]
    denominator = f[1]
    
    while numerator > 0:  
        unit_fraction = math.ceil(denominator / numerator)
        result.append(unit_fraction)  
        
        numerator = numerator * unit_fraction - denominator
        denominator = denominator * unit_fraction
    return result
#Improved version of the egyptian function, that tries to find a better representation
def improved_egyptian(f):
    original = egyptian(f)
    best = original
    best_length = len(original)
    for i in range(1 , f[0]):
        a = [i , f[1]]
        b = [(f[0]-i ) , f[1]]
        
        a_egypt = egyptian(a)
        b_egypt = egyptian(b)
        
        combined = a_egypt + b_egypt
        combined.sort()
        if (combined[-1]) < best[-1]:
            best = combined
            best_length = len(combined)
    return best   

#Function to express a list of integers as a fraction
def uncontinue(L):
    if not L:
        return [0, 1]
    if len(L) == 1:
        return [L[0], 1]
    
    num, den = uncontinue(L[1:])
    return [L[0] * num + den, num]

#Fraction to express a rational number in a list as a continued fraction
def continued_rat(frac):
    num, den = frac
    ans = []
    while den != 0:
        q = num // den
        ans.append(q)
        num, den = den, num - q * den

    return ans

