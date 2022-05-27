# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word1, word2):
     word1 = word1.lower()
     word2 = word2.lower()
     if(len(word1)==len(word2)):
         if(sorted(word1)!=sorted(word2)):
             return False
         else:
                if(word1[i]!=word2[i] for i in range(len(word1))):
                    return True
                else:
                    return False
    
     else:
         return False
print(find_anagram("tools","stoow"))

