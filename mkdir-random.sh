#!/bin/bash

# GENERATE RANDOM CHARACTER
#RANDOM_CHAR=`cat /dev/urandom |tr -dc 'a-zA-Z0-9'|head -c 1`
#random-char(){ cat /dev/urandom |tr -dc 'a-zA-Z0-9'|fold -w 1|head -n 1; }
random-char(){ cat /dev/urandom |tr -dc 'a-zA-Z0-9'|fold -w 1|head -n 1; }
RANDOMCHAR1 = random-char()
$RANDOMCHAR2 = random-char
echo $RANDOMCHAR1

# CREATE DIRECTORY TREE USING RANDOM CHARACTER
#mkdir -p {$RANDOMCHAR1,$RANDOMCHAR1}
