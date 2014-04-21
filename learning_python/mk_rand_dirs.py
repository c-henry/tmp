#! /usr/bin/python

import itertools
import os
import string
import random


# GENERATES RANDOM CHAR
def generator():
     return random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)

# SETUP NESTED DIRECTORY
dirs = [[generator()],
        [generator(), generator(), generator(), generator()],
        [generator(), generator(), generator(), generator()], 
        [generator(), generator(), generator(), generator(), generator()]]

# CREATE DIRECTORY STRUCTURE
for item in itertools.product(*dirs):
    os.makedirs(os.path.join(*item))
