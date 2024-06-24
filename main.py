#problem 1

# def cast_vote(votes, candidate):
#   if candidate not in votes:
#     votes[candidate] = 1
#   else:
#     votes[candidate] = votes[candidate]+1

#   return votes


# votes = {"Alice": 5, "Bob": 3}
# print(cast_vote(votes, "Gina"))

#problem 2

# def common_keys(dict1, dict2):
#   common = []
#   for k, v in dict1.items():
#     if k in dict2:
#       #print(k)
#       common.append(k)
      
#   return common


# dict1 = {"a": 1, "g": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)

'''
#problem 3
def get_highest_priority_task(tasks):
  highest = 0
  highestStr = ""
  listStr = []
  for k, v in tasks.items():
    if v > highest:
      v = highest
      highestStr = k

  
  # if highest in tasks:
  #   listStr.append(k)


  name = tasks.pop(highestStr)
  
  # name = ""
  # if len(listStr) > 1:
  #   listStr[0] > listStr[1]
  #   name = tasks.pop(listStr[1])

  return name


def get_highest_priority_task(tasks):
    if not tasks:
        return None
    highest_priority = max(tasks.values())
    highest_task = None
    for task, priority in tasks.items():
        if priority == highest_priority:
            if highest_task is None or task < highest_task:
                highest_task = task
    tasks.pop(highest_task)
    return highest_task
``


'''
# def get_highest_priority_task(tasks):
#   highest = 0
#   priority = ""

#   for i in tasks:
#      if tasks[i] > highest:
#        highest = tasks[i]
#        priority = i  

#   tasks.pop(priority)
#   return priority

# tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# print(tasks)

#problem 4

def count_occurrences(nums):
  count = {}
  for i in nums:
    if i not in count:
      count[i] = 1
    else:
      count[i] = count[i] + 1
  return count    

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))

#problem 5

def find_majority_element(elements):
  x = len(elements) / 2 
  count = {}
  for i in elements:
    if i not in count:
      count[i] = 1
    else:
      count[i] = count[i] + 1

  print(count)
  majority = 0
  for j in count:
    if count[j] > x:
      majority = j


  return majority

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
    
    
#problem 6

def hasDuplicates(nums):
  
  
  
  
  

