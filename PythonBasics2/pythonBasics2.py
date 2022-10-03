# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

import string
from typing import final


def count_threes(n):
  # YOUR CODE HERE
  multiples = {}
  multiples["3"] = 0
  multiples["6"] = 0
  multiples["9"] = 0
  countThree = 0
  countSix = 0
  countNine = 0
  maxCount = 0
  current = 0
  currentID = 0
  for i in n:
    if i == '3':
      countThree += 1
      up_dict = {"3":countThree}
      multiples.update(up_dict)
    elif i == '6':
      countSix += 1
      up_dict = {"6":countSix}
      multiples.update(up_dict)
    elif i == '9':
      countNine += 1
      up_dict = {"9":countNine}
      multiples.update(up_dict)
  for key,value in multiples.items():
    current = value
    if current > maxCount:
      maxCount = current
      currentID = key
  return int(currentID)


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  consec = {}
  finalConsec = []
  lastChar = ""
  finaChar = ""
  counter = 0
  maxCount = 0
  currentID = ""
  for x in s:
    if x == lastChar:
      if counter == 1:
        consec[x] = counter
      counter += 1
      up_dict = {x:counter}
      consec.update(up_dict)
    else:
      counter = 1
      lastChar = x
  for key,value in consec.items():
    current = value
    currentID = key
    if current > maxCount:
      maxCount = current
      finalConsec.clear()
      finalConsec.append(currentID)
    elif current == maxCount:
      finalConsec.append(currentID)
  return finalConsec


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE
  newString = s.lower().replace(' ', '')
  revString = newString[::-1]
  result = newString == revString
  return result