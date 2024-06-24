'''
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
