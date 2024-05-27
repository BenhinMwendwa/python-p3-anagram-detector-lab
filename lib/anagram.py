from collections import Counter

class Anagram:
    def __init__(self, word):
        
        self.word = word.lower()
        self.word_count = Counter(self.word)
    
    def match(self, possible_anagrams):
        
        correct_anagrams = []
        
        
        for candidate in possible_anagrams:
        
            candidate_count = Counter(candidate.lower())
            
            
            if self.word_count == candidate_count:
                correct_anagrams.append(candidate)
        
        return correct_anagrams


listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result) 
