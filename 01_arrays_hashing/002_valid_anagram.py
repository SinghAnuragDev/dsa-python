## Method: Hashing [T.C. -> O(n) || S.C. -> O(1)]
def valid_anagram(s, t):

    if len(s) != len(t): ## O(1)
        return False
      
    count = {} ## S.C -> O(1) , as the number of keys at max can be 26 and cannot grow more if 'n' grows.
    
    for char in s: ## O(n)
        if char in count: ## O(1)
            count[char] += 1
            continue
        
        count[char] = 1
        
        
    for char in t: ## O(n)
        if char in count: ## O(1)
            count[char] -= 1
            
            if count[char] < 0: ## O(1)
                return False
              
            continue
        
        return False
          
    return True

## Method: Sorting [T.C. -> O(nlogn) || S.C. -> O(n)]
def valid_anagram_sorting(s, t):
    return sorted(s) == sorted(t)

    ## Using sorted() creates new list.
    
    ## T.C.->sorted(s) O(n log n) + sorted(t) O(n log n) + comparing O(n) = O(n log n)
    
    ## S.C.->sorted(s) O(n) + sorted(t) O(n)
        
    ## O(n) + O(n) = O(n)
    
    
       
## Method: Using Counter(Collections)[T.C -> O(n) || S.C. -> O(1)]
from collections import Counter
def valid_anagram_collection(s, t):
    return Counter(s) == Counter(t)
  
    ## T.C.-> Counter(s) O(n) + Counter(t) O(n) + comparing at most 26 keys O(1) = O(n)
  
    ## S.C. -> Counter collection creates two dictionaries and compares them. 
    
    ## These dictionaries will at most have 26 keys just like Hashing Method. Therefore, S.C. of each dictionary will be O(1)
    
    ## So, Total S.C. -> O(1) 
  

## Method : Using Frequency method[T.C->O(n) || S.C. -> O(1)] , this method assumes letters are lowercase only. For uppercase, some indexes would be accepted while some wouldn't, e.g. ord('A') - ord('a') = 65 - 97 = -32, which will throw IndexError. But ord('Z') - ord('a') = 90 - 97 = -7, which is within index range of list of size 26, will get accepted although this will give us wrong answer as --> count[-7] = count[26 - 7] = count[19], which is the slot for 't'. So 'Z' is silently counted as 't' → no error here, but wrong answer.

## For uppercase or other characters, use the hashing, sorting, or Counter method.
# Note that List in Python accepts negative indexes too.

## a =       ['p', 'q', 'r', 's', 't']

## positive:   0    1    2    3    4
## negative:  -5   -4   -3   -2   -1

# A negative index '-i' refers to same slot as 'len(a) - i'.

def valid_anagram_frequency(s, t):
    count = [0] * 26 ## S.C. -> O(1), always 26 slots
    
    for ch in s: ## O(n)
        count[ord(ch) - ord('a')] += 1 ## O(1)
    
    for ch in t: ## O(n)
        count[ord(ch) - ord('a')] -= 1 ## O(1)
        
    return all(x == 0 for x in count) ## O(26) = O(1)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().split()
        
    s = data[0]
    t = data[1]
    
    print(valid_anagram(s, t))
    
## Extras

# If interview asks to ignore uppercase and lowercase and mixes 'D' and 'd' in inputs, like s = Dog; t = god, then convert both strings to lowercase first using s.lower() and t.lower().