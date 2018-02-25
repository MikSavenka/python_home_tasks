# Get input arguments (sys.argv) and print them and their sum
import sys

s = sum(int(i) for i in sys.argv[1:])
args = ''
for arg in sys.argv[1:]:
    args += arg + ", "
print("Got {0}. Sum is {1}.".format(args[:-2], s))
