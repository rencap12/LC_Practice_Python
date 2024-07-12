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
