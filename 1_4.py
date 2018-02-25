# Get 2 numbers as input arguments and print result of division with 2 fractional digits
import sys

divident = sys.argv[1]
divider = sys.argv[2]


print("{0:.2f}".format(int(divident)/int(divider)))