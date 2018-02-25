# Get string as input argument and verify it contains: letter a, any digit, word 'apple'
import sys

input = sys.argv[1:]

has_a = 'a' in input[0]
has_digit = False
for letter in input[0]:
    if letter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        has_digit = True
has_apple = 'apple' in input[0]

print("Input string contains letter a: {0}, any digit: {1}, word 'apple': {2}".format(has_a, has_digit, has_apple))