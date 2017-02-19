#!/usr/bin/python

import os
from pathlib import Path
import exec_sql
import format_json
from search_duplication import SearchDuplication
#from exec_sql import *

inputFile = "./vm_vrResult1.json"
outputFile = "./vm_vrResult2.json"

jsonFile = "./vm_vrResult.json"
outputLog = "./vm_vr.log"



if __name__ == "__main__":
	s = exec_sql.ExecSQL()
	new_data = s.structDataFromSQL()

	j = format_json.FormatJson()
	j.readFile(inputFile)

	d = SearchDuplication(j.data,new_data)
	d.searchNewVMs()
	
	#j.data.update(data)
	#j.dumpInJson(outputFile,j.data)	





