'''
# # 1
# def sum_of_number_strings(nums):
#   sum = 0
#   for n in nums:
#     sum += int(n)
#   return sum

# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)


# # 2
# def remove_duplicates(nums):
#   singles = []
#   i = 0
#   while i < len(nums):
#     singles.append(nums[i])

#   #skip if still duplicate
#     while i + 1 < len(nums) and nums[i] == nums[i + 1]:
#       i += 1
      
#     i += 1 #skip to next new one
#   return singles


# nums = [1,1,1,2,3,4,4,5,6,6]
# no_dups = remove_duplicates(nums)
# print(no_dups)

# s[::-1]
# 3

1) Create an empty list for the letters
2) Loop through the string, and add any letters to the list
3) Make an index variable, set to end of letters list
4) Create an empty results string
5) Loop through each character in the original string
  a) If the char was a letter:
     i) add the value at letters[index] to results
    ii) reduce index by 1
  b) Otherwise, add the char itself to results
6) Return results




#isAlpha
def reverse_only_letters(s):
  letters = []
  for ch in s:
    if ch.isalpha():
      letters.append(ch)

  index_let = len(letters) - 1
  results = ""
  for ch in s:
    if ch.isalpha():
      results += letters[index_let]
      index_let -= 1
    else:
      results += "-"

  return results


s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

# HI WE GOT CUT OFF - BUT WHAT WWAS YOUR QUESTION?
#^^^^
#I share with you two solutions for problem  3
#thanks!
# You're welcome

Solution 1:
def reverse_only_letters(s):
  letters = []  # Collect letters 
  for c in s:
      if c.isalpha():
          letters.append(c)

  result = ""
  letters_index = len(letters) - 1  # Start from the end of the letters list

  for c in s:
      if c.isalpha():
          result += letters[letters_index]
          letters_index -= 1
      else:
          result += c
  return result

Solution 2: Using only one for loop
def reverse_only_letters(s):
    letters = [c for c in s if c.isalpha()] 
    result = ""  
    letters_index = len(letters) - 1  
    for c in s:  
        if c.isalpha():  
            result += letters[letters_index]  
            letters_index -= 1  
        else:
            result += c  
    return result  
'''
