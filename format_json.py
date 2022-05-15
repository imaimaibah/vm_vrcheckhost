import os
import json

class FormatJson:
	def __init__(self):
		self.data = {}

	def readFile(self,file):
		if os.path.isfile(file):
			with open(file) as data_file:    
				self.data = json.load(data_file)
			return 1
		else:
			return 0

	def parseJson(self):
		pass

	def dumpInJson(self,ofile,newData):
		with open(ofile, 'w') as outfile:
			outfile.write(json.dumps(newData, sort_keys=True, indent=4))

	def displayInJson(self,data):
		print(json.dumps(data, sort_keys=True, indent=4))

