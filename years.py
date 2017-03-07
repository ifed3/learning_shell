#!/usr/bin/python
"""Prints number of years till 100"""

import sys

# Variable definition is done with the equal sign
# argv is the list of arguments entered at runtime
# argv[0] is the path of the script being run
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = raw_input('What is your name? ')

if len(sys.argv) > 2:
    age = int(sys.argv[2]) # Type conversion is done as str() or float()
else:
    age = int(raw_input('How young are you? '))

if age == 100:
    comment = "You're already on the dot"
elif age < 100:
    comment = "You will be 100 in {} years".format(100 - age)
else:
    comment = "You were already 100 {} years ago".format(age - 100)

print "Hello, {0}. {1}!".format(name, comment)
