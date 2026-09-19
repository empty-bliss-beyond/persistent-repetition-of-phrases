# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

def count_bits(n: int) -> int:

    # Idea: convert to binary with a built-in function,
    # then cast to string and count '1' this way
    to_binary: str = str(bin(n))
    return to_binary.count("1")