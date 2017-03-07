#!/bin/sh

# For Loops
for i in 1 2 3 4 5
do
    echo "Looping through values $i"
done

# What should this segment do? Expect that shell would act on each character
# So the iteration would be hello 1 then all current files then 2 goodbye
for i in hello 1 * 2 goodbye
do
    echo "Looping through values $i"
done