#!/bin/sh

# Variables are defined with intermediate spacing between the variable name, value and equal sign
# After being defined, the variable is called with a "$" before the name

# Shell isn't a statically typed language and variables need not be declared
# Reading an undeclared variables produces an empty string

# Variables can be exported to be utilized by other programs with the export command
# Variables can be imported into a shell session by sourcing a script with the "." command
# The .profile or .bash_profile is initalized with each shell session and variables are sourced 
# from it to set up current shell environment variables

DOPE_BAND="Sylvan Esso"
echo $DOPE_BAND

# Read retrieves line from stdin
# Read places entire line being read in quotes to maintain spacing
echo What is your occupation?
read MY_JOB
echo "Good luck, robots will soon be a better $MY_JOB than you are!"