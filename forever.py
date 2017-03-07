#!/usr/bin/python
"""Script runs forever until user interrupted"""

import time

counter = 0

while 1: # 1 is a truthy value
    time.sleep(1)
    counter += 1

    print 'Script has been running for {} seconds'.format(counter)
    