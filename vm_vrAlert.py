#!/usr/bin/python

import os
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
	s = exec_sql.ExecSQL()
	new_data = s.structDataFromSQL()

	h = format_json.FormatJson()
	h.readFile(inputFile)

	i = SearchDuplication(h.data,new_data)
	new_vms = i.searchNewVMs()

	n = LogWrite(outputLog)
	n.logWrite(new_vms)

	#j.data.update(data)
	#j.dumpInJson(outputFile,j.data)
