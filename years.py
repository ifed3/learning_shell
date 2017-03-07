#!/usr/bin/python
"""Prints number of years till 100"""

import sys

# Variable definition is done with the equal sign
# argv is the list of arguments entered at runtime
# argv[0] is the path of the script being run
name = sys.argv[1]
age = int(sys.argv[2]) # Type conversion is done as str() or float()
diff = 100 - age

print "Hello {0}, you will be 100 in {1} years".format(name, diff)
