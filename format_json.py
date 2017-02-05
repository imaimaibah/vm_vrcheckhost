from pathlib import Path
import json

class FormatJson:
	def __init__(self):
		pass

	def readFile(self):
		my_file = Path("./vm_vrResult.json")
		if my_file.is_file():
			with open('vm_vrResult.json') as data_file:    
				oldData = json.load(data_file)

		return oldData

	def parseJson():
		pass

	def dumpInJson():
		with open('vm_vrResult.json', 'w') as outfile:
			json.dump(data,outfile)

