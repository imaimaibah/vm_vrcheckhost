#!/usr/bin/python

import os
from pathlib import Path
import re
import exec_sql
import format_json
#from exec_sql import *



if __name__ == "__main__":
	fj = format_json.FormatJson()
	print(fj.readFile())

	s = exec_sql.ExecSQL()
	print(s.data)
