# https://www.codewars.com/kata/5edc8c53d7cede0032eb6029/train/python

def solve(n: int) -> int:
    
    # Given n, find m² so that n + m² = k²
    # Rewrite: n = k² - m² = (k + m)(k - m)
    # Let a = k - m (1), b = k + m (2)
    # Subtract (1) from (2) to isolate m -> 2m = b - a -> m = (b - a) / 2
    
    # To find (a, b), we'll have to look for factor pairs of n
    # From napkin math, b - a must be even, so a and b must have the same parity
    # From napkin math, I have to choose a, b that are as close as they can be
    # This suggests working with sqrt(n) might be a thing
    
    sqrt_n: int = int(n ** 0.5)
    
    for a in range(sqrt_n, 0, -1):
        
        # This finds pair (a, b) so that ab = n
        if n % a == 0:
            b: int = n // a
            
            # Now we check for condition: a and b must have the same parity
            # I apparently have to check against b - a = 0 too?
            if a != b and (b - a) % 2 == 0:
                m: int = (b - a) // 2
                return m ** 2
    
    return -1
                