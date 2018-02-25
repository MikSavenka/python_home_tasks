# Get one input string argument and print its letters in table format: 3 letters per line delimited by 4 spaces
import sys

input = sys.argv[1:]
word = input[0]

for i in range(0, len(word)):
    print("{0}    ".format(word[i]), end="")
    if ((i+1) % 3 == 0):
        print('\n')
