## TLE(70/79)[T.C.-> O(n²) || S.C.-> O(n)]
def contains_duplicate_using_list(nums):
    distinct = [] ## S.C. -> O(n)
    
    for item in nums: ## O(n)
        if item not in distinct: ## O(n), list search checks every element
            distinct.append(item) ## O(1)
            continue
        
        return True
      
    return False

## [T.C.-> O(n) || S.C.-> O(n)]
def contains_duplicate_using_set(nums):
    seen = set() ## S.C.-> O(n), worst case all elements are distinct. 
    
    for item in nums: ## O(n)
        if item in seen: ## O(1)
            return True
        
        seen.add(item) ## O(1)
  
    return False       

## T.C.-> O(n) || S.C. -> O(n)
def contains_duplicate_using_one_liner(nums):
    
    
    return len(set(nums)) != len(nums)

    ## set(nums) -> O(n), goes through nums one by one, adding each to a new set
    
    ## len(set(nums)) -> O(1), Python keeps track of the size, so it doesn't count anything. 
    
    ## len(nums) -> O(1), same reason as above.
    
    ## comparison -> O(1), len(set(nums)) is a number, similarly len(nums) is a number and both are being compared, e.g. 3 != 4. This takes O(1).
    
    ## Total T.C. = O(n) + O(1) + O(1) + O(1) = O(n).
    
    ## S.C. = O(n), set(nums) creates a set of upto 'n' elements.
    

## T.C.-> O(nlogn) || S.C.-> O(n)
def contains_duplicate_using_sorting(nums):

    nums.sort() ## T.C.-> O(nlogn) || S.C.-> O(n), worst case, Python's built in sort uses a temporary buffer.
    
    ## nums.sort() also modifies input list.
    
    for i in range(1, len(nums)) : ## O(n-1) = O(n)
        if nums[i] == nums[i - 1]: ## O(1)
            return True
          
    return False
  
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(contains_duplicate_using_one_liner(nums))
               