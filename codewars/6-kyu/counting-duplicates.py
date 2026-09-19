# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

from collections import Counter

def duplicate_count(text: str) -> int:
    
    # Idea: use a Counter
    counter: Counter = Counter(text.lower())
    
    # And now use a list where values are either 0 (no duplicates) or 1
    return sum(1 for dupes in counter.values() if dupes > 1)