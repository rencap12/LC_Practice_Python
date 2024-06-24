'''
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
'''
