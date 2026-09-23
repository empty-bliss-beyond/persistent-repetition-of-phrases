# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
# I'm bored. I'll try doing this with some OOP
import re

class PigLatinProcessor:
    def __init__(self, sentence: str):
        
        # Find all 
        self.tokens: list[str] = re.findall(
                r"[A-Za-z]+|[^A-Za-z]+",
                sentence
            )
        # print(self.tokens)
    
    def process(self):
        
        strategy = None
        transformed_sentence: str = str()
        
        # Check all "tokens"
        for token in self.tokens:
            
            # Check against actual characters
            if re.match(r"[A-Za-z]+", token):
                strategy = WordStrategy()
            else:
                strategy = NotWordStrategy()
        
            transformed_sentence += strategy.transform(token)
        
        return transformed_sentence
    
class WordStrategy:
    def transform(self, word: str) -> str:
        if len(word) == 1:
            return word + "ay"
        
        first_letter: str = word[0]
        everything_else: str = word[1:]

        return everything_else + first_letter + "ay"
    
class NotWordStrategy:
    def transform(self, not_a_word: str) -> str:
        return not_a_word


def pig_it(text: str) -> str:
    return PigLatinProcessor(text).process()