#!/usr/bin/python

import os
from pathlib import Path
import exec_sql
import format_json
#from exec_sql import *



if __name__ == "__main__":
	s = exec_sql.ExecSQL()
	data = s.structDataFromSQL()

	j = format_json.FormatJson()
	j.readFile("./vm_vrResult1.json")
	j.data.update(data)
	j.dumpInJson("./vm_vrResult2.json",j.data)	


