#!/bin/sh

# Variables are defined with intermediate spacing between the variable name, value and equal sign
# After being defined, the variable is called with a "$" before the name

DOPE_BAND="Sylvan Esso"
echo $DOPE_BAND

# Read retrieves line from stdin
echo What is your occupation?
read MY_JOB
echo "Good luck, robots will soon be a better $MY_JOB than you are!"