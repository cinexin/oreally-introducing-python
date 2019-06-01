'''Deque = Double ended queue
It contains features of both stack and queue elements
It's useful when you want to delete elements from either end of a sequence'''

# Let's use it to check if a word is a palindrome
from collections import deque


def palindrome(word):

    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


def control_palindrome_pass_tests(expected_value, func, word):
    if func(word) == expected_value:
        print("OK!")
    else:
        print("KO!")
        exit(-1)


print("TESTS FIRST PALINDROME FUNCTION....")
control_palindrome_pass_tests(True, palindrome, 'a')
control_palindrome_pass_tests(True, palindrome, 'racecar')
control_palindrome_pass_tests(True, palindrome, '')
control_palindrome_pass_tests(True, palindrome, 'radar')
control_palindrome_pass_tests(False, palindrome, 'halibut')
control_palindrome_pass_tests(False, palindrome, 'Hollywood')
control_palindrome_pass_tests(True, palindrome, '224422')


def another_palindrome(word):
    return word == word[::-1]


print("TESTS SECOND PALINDROME FUNCTION....")
control_palindrome_pass_tests(True, palindrome, 'a')
control_palindrome_pass_tests(True, palindrome, 'racecar')
control_palindrome_pass_tests(True, palindrome, '')
control_palindrome_pass_tests(True, palindrome, 'radar')
control_palindrome_pass_tests(False, palindrome, 'halibut')
control_palindrome_pass_tests(False, palindrome, 'Hollywood')
control_palindrome_pass_tests(True, palindrome, '224422')

exit(0)