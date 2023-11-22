import os
import sys

te = sys.argv[1]
ls = sys.argv[2]

print(te)
print(ls)

BRANCH = os.environ.get('BRANCH')
test = str(os.environ.get('TEST'))
test2 = test.format(BRANCH)
print(BRANCH)
print(test)
print(test2)
