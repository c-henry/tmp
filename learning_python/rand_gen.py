#! /usr/bin/python

import string
import random

#def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))
#
#print id_generator()

print "string.ascii_lowercase"
print string.ascii_lowercase
print "string.ascii_uppercase"
print string.ascii_uppercase
print "string.digits"
print string.digits
print "string.ascii_uppercase + string.digits"
print string.ascii_uppercase + string.digits + string.ascii_lowercase 


print "random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)"
print random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
print random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)


