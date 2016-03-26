import sys
x="test"
try:
    print(x+1)
except:
    print("Unexpected error:\n", sys.exc_info()[0])
    raise