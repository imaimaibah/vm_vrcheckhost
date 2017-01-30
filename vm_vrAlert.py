#!/usr/bin/python

import os 
from pathlib import Path
import json
import re
import time

def readFile():
	my_file = Path("./vm_vrResult.json")
	if my_file.is_file():
		with open('vm_vrResult.json') as data_file:    
			oldData = json.load(data_file)
#			print(json.dumps(oldData,sort_keys=True, indent=4))
#	else:
#		print("No")

	return oldData


def structDataFromSQL():
	localtime = int(time.time())
	data = {}
	data_s = {localtime: {}}
	f = os.popen("cat result.txt")

#####
	for line in f.readlines():
		if re.match(r'^(r-[^\s]*)',line):
			line = line.rstrip('\n')
			element = re.split(r"\t+",line);
			vr_name = element[0]
			onHost = element[2]
			network_id = element[3]
			vm_name = element[4]
			vm_instance_name = element[5]

			if vr_name not in data:
				data[vr_name] = {'host': onHost, 'network_id': set(), 'vm_name':set()}

			data[vr_name]['network_id'].add(network_id)
			data[vr_name]['vm_name'].add(vm_name)
####

	for key in data:
		data[key]['network_id'] = list(data[key]['network_id'])
		data[key]['vm_name'] = list(data[key]['vm_name'])

	data_s[localtime] = data

	return data_s

def dumpInJson():
	with open('vm_vrResult.json', 'w') as outfile:
		json.dump(data,outfile)


def restructNewData(oldData,newData):
	pass
	

def outputAlerts():
	pass


if __name__ == "__main__":
	flag = 1
	oldData = readFile()
	newData = structDataFromSQL()
	#outputAlerts(newData)

	if flag:
		newData = compareResult(oldData,newData)


