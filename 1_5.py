# Get list arguments in sys.argv and return all of them as one sentence starting with Capital letter and ending with dot
import sys

args = sys.argv[1:]
for arg in args:
    result = arg.split()[0][0].upper() + arg.split()[0][1:] + " "
    result = result + ' '.join(word for word in arg.split()[1:])
    result = result + ". "
    print(result, end="")