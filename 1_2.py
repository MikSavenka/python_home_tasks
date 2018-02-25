# Get one input string argument and cut one word from the beginning and from the end:
import sys

if sys.argv.__len__() < 3:
    cut = sys.argv[1:]
else:
    cut = sys.argv[2:-1]
result = ''
for arg in cut:
    result += arg + " "

print(result[:-1])
