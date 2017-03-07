#!/usr/bin/python
"""Prints number of years till 100"""

# import sys The system module is no longer needed at the moment
import optparse # Use in creating script options

parser = optparse.OptionParser()
parser.add_option('-n', '--name', dest='name', help='Provide your name')
parser.add_option('-a', '--age', dest='age', help='Provide your age', type=int)

(options, args) = parser.parse_args()

if not options.name:
    options.name = raw_input('What is your name? ')

if not options.age:
    options.age = int(raw_input('How young are you? '))

# Use tuple for multi variable definition
(name, age) = (options.name, options.age)

if age == 100:
    comment = "You're already on the dot"
elif age < 100:
    comment = "You will be 100 in {} years".format(100 - age)
else:
    comment = "You were already 100 {} years ago".format(age - 100)

print "Hello, {0}. {1}!".format(name, comment)
