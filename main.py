
# problem 1
# def is_long_pressed(name, typed):

#   nums1_pointer = 0
#   nums2_pointer = 0

#   while nums1_pointer < len(name) and nums2_pointer <   len(typed):
#   # <if conditional>
#     if name[nums1_pointer] == typed[nums2_pointer]:
#         # <operation>
#         nums1_pointer += 1
#         nums2_pointer += 1
#     elif nums2_pointer > 0 and typed[nums2_pointer] == typed[nums2_pointer-1]:
#       nums2_pointer +=1
#     else:
#         # <operation>
#       return False

#   return True

# name = "alex"
# typed = "aaleex"
# print(is_long_pressed(name, typed))

# name2 = "saeed"
# typed2 = "ssaaedd"
# print(is_long_pressed(name2, typed2))

# name3 = "courtney"
# typed3 = "courtney"
# print(is_long_pressed(name3, typed3))

# # problem 2
# def find_content_children(s, g):
#   g.sort()
#   s.sort()
#   nums1_pointer = 0
#   nums2_pointer = 0
#   count = 0

#   while nums1_pointer < len(s) and nums2_pointer < len(g):
#     # <if conditional>
#     if g[nums1_pointer] <= s[nums2_pointer]:
#         # <operation>
#       nums1_pointer += 1
#       nums2_pointer += 1
#       count +=1

#         # <operation>
#   return count

# g = [1,1]
# s = [2,2,2]
# # There are 2 children and 3 cookies
# # child `0` has a greed factor of 1
# # cookie `0` has a size of 2 --> content child

# # child `1` has a greed factor of 1
# # cookie `1` has a size of 1 --> content child

# print(find_content_children(s, g))
# Output: 2


# def check(s, front, back):
#   while front < back:
#     if s[front] != s[back]:
#       return False
#     front
#   # WHY IS THIS HARD LMAO jk we got this :)


# def valid_palindrome(s):
#   base = s[::-1]
#   if base == s:
#     return True

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

# def count_mississippi(limit):
#   for num in range(1, limit):
#     print( f"{num} mississippi")

# count_mississippi(6)

# def swap_ends(my_str):
#   # my_str[0] my_str[-1]
#   # return my_str[-1] + my_str[1:-1] + my_str[0] 
#   new_str = ""
#   new_str += my_str[-1]
#   for character in my_str[1:-1]:
#     new_str += character
#   new_str += my_str[0]
#   return new_str

# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)

# # Problem 3: 
# def is_pangram(my_str):
#   new_str = my_str.replace(" ", "")
#   s = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", 'y', "z"}

#   return all(i in new_str for i in s)

# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))
# return my_str[::-1]

# def reverse_string(my_str):
#   return my_str[::-1]

# my_str = "live"
# print(reverse_string(my_str))

# def first_unique_char(my_str):
#   freq = {}
#   for char in my_str:
#     if char not in freq:
#       freq[char] = 1
#     else:
#       freq[char] += 1
#   for key, value in freq.items():
#     if value == 1:
#       return my_str.index(key)
#   else:
#     return -1

# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))

# Problem 6:

# def min_distance(words, word1, word2):
#   w1_position = 0
#   w2_position = 0

#   for i, word in enumerate(words):
#     if word == word1:
#       w1_position = i
#     if word == word2:
#       w2_position = i

#   return abs(w2_position - w1_position)
  
# words = ["the", "quick", "brown", "fox", "jumped", "the"]
# dist1 = min_distance(words, "quick", "jumped") # 1, 4
# dist2 = min_distance(words, "the", "jumped")
# print(dist1) # 5, 4
# print(dist2)

# words2 = ["code", "path", "code", "contribute",  "practice"]
# dist3 = min_distance(words2, "code", "practice")
# print(dist3)

# def match_made(dictionary):
#   for key, value in dictionary.items():
#     print( f"{key} and {value} are a perfect match.")

# to_pass = {
#   "Peanut butter": "Jelly",
#   "Spongebob": "Patrick",
#   "Ash": "Pikachu"
# }

# match_made(to_pass)

# def remove_char(s, n):
#   return s[:n] + s[n+1:]

# s = "typpo"
# fixed_s = remove_char(s, 2)
# print(fixed_s)

# # Problem 3
# def vowel_count(s):
#   vowels = {'a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"}

#   vowel_cnt = 0
#   for i in s: 
#     if i in vowels:
#       vowel_cnt += 1
  
#   return vowel_cnt
      
# my_str = "hello world"
# my_str2 = "aAaAaAaAAA"
# my_str3 = "ths strng s mssng vwls"

# count1 = vowel_count(my_str)
# print(count1)
# count2 = vowel_count(my_str2)
# print(count2)
# count3 = vowel_count(my_str3)
# print(count3)

# def reverse_sentence(sentence):
#   words = sentence.split()
#   revWrds = words[::-1]
#   to_pass = "\""""
#   to_pass += " ".join(revWrds)
#   to_pass += "\""
#   return to_pass

# sentence = "I solemnly swear I am up to no good"
# #reverse_sentence(sentence)
# print(reverse_sentence(sentence))


# def compress_string(my_str):
#   frequency = {}
#   compress = ""
#   for character in my_str:
#     if character not in frequency:
#       frequency[character] = 1
#     else:
#       frequency[character] +=1
#   for key, value in frequency.items():
#     compress += key
#     compress += str(value)
#   if len(compress) >= len(my_str):
#     return my_str
#   else:
#     return compress


# my_str = "aaaaabbcccd"
# compressed_Str = compress_string(my_str)
# print(compressed_Str)

# my_str2 = "abcde"
# compressed_Str2 = compress_string(my_str2)
# print(compressed_Str2)

#Problem 6: 

# def find_the_needle(haystack, needle):
#   if needle in haystack:
#     return haystack.index(needle)
#   else:
#     return -1


# haystack = "tobeornottobe"
# needle = "be"
# print(find_the_needle(haystack, needle))

# haystack2 = "leetcode"
# needle2 = "leeto"
# print(find_the_needle(haystack2, needle2))

def choose_pokemon(my_pokemon):
  for pokemon in my_pokemon:
    print(f"{pokemon} I choose you!")


to_pass = ["Pikachu", "Charizard ", "Eevee"]
choose_pokemon(to_pass)

#nice working with you

# #problem 1

# # def cast_vote(votes, candidate):
# #   if candidate not in votes:
# #     votes[candidate] = 1
# #   else:
# #     votes[candidate] = votes[candidate]+1

# #   return votes

# # votes = {"Alice": 5, "Bob": 3}
# # print(cast_vote(votes, "Gina"))

# #problem 2

# # def common_keys(dict1, dict2):
# #   common = []
# #   for k, v in dict1.items():
# #     if k in dict2:
# #       #print(k)
# #       common.append(k)

# #   return common

# # dict1 = {"a": 1, "g": 2, "c": 3}
# # dict2 = {"b": 4, "c": 5, "d": 6}
# # common_list = common_keys(dict1, dict2)
# # print(common_list)


# #problem 3
# def get_highest_priority_task(tasks):
#   highest = 0
#   highestStr = ""
#   listStr = []
#   for k, v in tasks.items():
#     if v > highest:
#       v = highest
#       highestStr = k

#   # if highest in tasks:
#   #   listStr.append(k)

#   name = tasks.pop(highestStr)

#   # name = ""
#   # if len(listStr) > 1:
#   #   listStr[0] > listStr[1]
#   #   name = tasks.pop(listStr[1])

#   return name

# def get_highest_priority_task(tasks):
#     if not tasks:
#         return None
#     highest_priority = max(tasks.values())
#     highest_task = None
#     for task, priority in tasks.items():
#         if priority == highest_priority:
#             if highest_task is None or task < highest_task:
#                 highest_task = task
#     tasks.pop(highest_task)
#     return highest_task

# # def get_highest_priority_task(tasks):
# #   highest = 0
# #   priority = ""

# #   for i in tasks:
# #      if tasks[i] > highest:
# #        highest = tasks[i]
# #        priority = i

# #   tasks.pop(priority)
# #   return priority

# # tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
# # perform_task = (get_highest_priority_task(tasks))
# # print(perform_task)

# # perform_task = (get_highest_priority_task(tasks))
# # print(perform_task)

# # perform_task = (get_highest_priority_task(tasks))
# # print(perform_task)

# # print(tasks)

# #problem 4

# def count_occurrences(nums):
#   count = {}
#   for i in nums:
#     if i not in count:
#       count[i] = 1
#     else:
#       count[i] = count[i] + 1
#   return count

# nums = [1, 2, 2, 3, 3, 3, 4]
# print(count_occurrences(nums))

# #problem 5

# def find_majority_element(elements):
#   x = len(elements) / 2
#   count = {}
#   for i in elements:
#     if i not in count:
#       count[i] = 1
#     else:
#       count[i] = count[i] + 1

#   print(count)
#   majority = 0
#   for j in count:
#     if count[j] > x:
#       majority = j

#   return majority

# elements = [2, 2, 1, 1, 1, 2, 2]
# print(find_majority_element(elements))

# #problem 6

# def hasDuplicates(nums):
# testing for new repo push

# # Write a function print_list() that takes in a list lst as a parameter and prints out each item in the list.

# # def print_list(lst):
# #   for str in lst:
# #     print(str)

# # lst = ["squirtle", "gengar", "charizard", "pikachu"]
# # print_list(lst)
# """
# Write a function doubled() that takes in a list of integers lst as a parameter and prints each item in the list multiplied by two.

# def doubled(lst):
#     pass


# # def doubled(lst):
# #   for str in lst:
# #     print(str*2)

# # lst = [2,4,6]
# # doubled(lst)

# # Modify the function doubled() so that instead of printing the items, it returns a new list of the doubled numbers.

# # def doubled(lst):
# #   new_list = []
# #   for i in lst:
# #     new_i=i*2
# #     new_list.append(new_i)
# #   return new_list

# # lst = [1,2,3]
# # new_lst = doubled(lst)
# # print(new_lst)

# # Write a function flip_sign() that takes in a list of integers lst as a parameter and returns a new list where each number in the original list has been multiplied by -1.

# # def flip_sign(lst):
# #     new_list = []
# #     for i in lst:
# #       new_i=i*-1
# #       new_list.append(new_i)
# #     return new_list

# # lst = [1,-2,-3,4]
# # flipped_lst = flip_sign(lst)
# # print(flipped_lst)

# Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.

# def max_difference(lst):
#     pass


# # def max_different(lst):
# #   max_diff = max(lst) - min(lst)
# #   return(max_diff)

# # list = [5,22,8,10,2]
# # max_different(list)

# # Write a function count_less_than() that takes in a list of integers numbers and an integer threshold as parameters and returns the number of items in numbers that are less than threshold.

# # def count_less_than(numbers, threshold):
# #   count= 0
# #   for i in numbers:
# #     if i < threshold:
# #       count+=1
# #   return count

# # numbers = [12,8,2,4,4,10]
# # counter = count_less_than(numbers,5)
# # print(counter)

# # Write a function get_evens() that takes in a list of integers lst as a parameter and returns a list of all even numbers in the list.

# # def get_evens(lst):
# #   new_list = []
# #   for i in lst:
# #     if i % 2 == 0:
# #       new_list.append(i)
# #   return new_list

# # lst = [1,2,3,4]
# # evens_lst = get_evens(lst)
# # print(evens_lst)

# # Write a function multiples_of_five() that prints out multiples of 5 between 1 and 100 (inclusive).

# # def multiples_of_five():
# #     pass

# def multiples_of_five():
#     for i in range(1, 101):
#         if i % 5 == 0:
#             print(i)

# # to push to the different repo
'''

