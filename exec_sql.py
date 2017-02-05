import time
import os 

class ExecSQL:

	def __init__(self):
		self.data = {}

	def readData(self, cmd):
		return os.popen(cmd)

	def structDataFromSQL(self):
		localtime = int(time.time())
		data_s = {localtime: {}}
		f = self.readData("cat result.txt")
		for line in f.readlines():
			structData(line)

		data_s[localtime] = self.data

		return data_s

	def structData(self, line):
		if re.match(r'^(r-[^\s]*)',line):
			line = line.rstrip('\n')
			element = re.split(r"\t+",line);
			vr_name = element[0]
			onHost = element[2]
			network_id = element[3]
			vm_name = element[4]
			vm_instance_name = element[5]

			if vr_name not in self.data:
				self.data[vr_name] = {'host': onHost, 'network_id': set(), 'vm_name':set()}

			self.data[vr_name]['network_id'].add(network_id)
			self.data[vr_name]['vm_name'].add(vm_name)

		for key in self.data:
			self.data[key]['network_id'] = list(self.data[key]['network_id'])

		self.data[key]['vm_name'] = list(sel.fdata[key]['vm_name'])
