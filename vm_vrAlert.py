#!/usr/bin/python

import os
import sys
import collections
from pathlib import Path
import exec_sql
import format_json
from search_duplication import SearchDuplication
from log_write import LogWrite

inputFile = "./vm_vrResult1.json"
outputFile = "./vm_vrResult2.json"

jsonFile = "./vm_vrResult.json"
outputLog = "./vm_vr.log"



if __name__ == "__main__":

	### Execute EQL to obtain a new data ###
	s = exec_sql.ExecSQL()
	new_data = s.structDataFromSQL()

	h = format_json.FormatJson()
	h.readFile(inputFile)

	i = SearchDuplication(h.data,new_data)
	new_vms = i.searchNewVMs()

	n = LogWrite(outputLog)
	n.logWrite(new_vms)

	dummyData = new_data.copy()
	dummyData.update(h.data)
	keys = sorted(dummyData, reverse=True)
	outputData = {}
	if len(sys.argv) > 1:
		num = int(sys.argv[1])
	else:
		num = 5

	for i in keys[:num]:
		outputData[i] = dummyData[i]
		
	h.dumpInJson(jsonFile,outputData)
	#h.displayInJson(outputData)
