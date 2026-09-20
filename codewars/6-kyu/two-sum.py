# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

def two_sum(numbers: list[int], target: int) -> tuple[int, int]:
    
    # Had some issues with duplicate numbers with my initial dict approach
    # Let's try storing seen numbers as keys and their indexes as values
    cache: dict[int, int] = dict()
    
    for index, number in enumerate(numbers):
        complement = target - number
        
        # If our complement is already in our cache, return it
        if complement in cache:
            return (cache[complement], index)
        
        # Otherwise... add number: index to cache
        cache[number] = index
    
    # Question says we're guaranteed to find an answer, so I won't bother with writing safer code