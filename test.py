#!/usr/bin/python

import os 

def readFile():
	return os.popen("cat result.txt")

f = readFile()
for line in f.readlines():
	print(line)


