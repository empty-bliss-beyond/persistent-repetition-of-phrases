# https://www.codewars.com/kata/664bb0ec2b1fc1bf9d51b5a0/train/python

from math import isqrt

# Seeing how relying solely on isqrt times it out, I'll probably have to filter numbers before getting to isqrt
# Also, seeing how there are 2.5 million calls of numbers between 0 to 1000, caching them feels just right

# Caching
SQUARES_BELOW_1000: list[bool] = [False] * 1000

for n in range(32):
    SQUARES_BELOW_1000[n ** 2] = True
    
# Filtering
# This works by caching all possible least significant n bits that can belong to a square number
# For 4 LSB, we're removing 12/16 of isqrt() checks
# For 8 LSB, we're removing 212/256 of isqrt() checks
# It seems to approach 5/6 as I increase the number of LSB to look at, but the search space grows exponentially
# I'll yolo numbers around 6?

BITS: int = 6
SQUARE_RESIDUES = frozenset(n ** 2 & ((2 ** BITS) - 1) for n in range(2 ** BITS))

def is_square(n: int) -> bool:
    
    if n < 1000:
        return SQUARES_BELOW_1000[n]
    
    # (n & 15) is equivalent to (n % 16)
    # Check against residues first
    if n & ((2 ** BITS) - 1) not in SQUARE_RESIDUES:
        return False
        
    # If it's a potential square number, finally run isqrt()
    k: int = isqrt(n)
    return k ** 2 == n
    
    