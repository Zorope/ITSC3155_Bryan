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


def count_threes(n):
  # YOUR CODE HERE
  count = 0
  for i in range(0,n+1):
    if i%3 == 0 and i !=0:
      count = count+1
  return count


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  lastChar = ""
  finaChar = ""
  counter = 0
  maxCount = 0
  for x in s:
    if x == lastChar:
      counter += 1
      if counter > maxCount:
        maxCount = counter
        finalChar = x
    else:
      counter = 1
      lastChar = x
  return finalChar


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