class SearchDuplication():
	def __init__(self,old,new):
		self.newVMs = set()
		self.oldVMs = set()
		self.old = old
		self.new = new


	def _createSetOfNewVms(self):
		new = self.new
		for i in new:
			for m in new[i]:
				self.newVMs.update(new[i][m]['vm_name'])


	def _createSetOfOldVms(self):
		old = self.old
		for i in old:
			for m in old[i]:
				self.oldVMs.update(old[i][m]['vm_name'])


	def searchNewVMs(self):
		self._createSetOfNewVms()
		self._createSetOfOldVms()
		alertVMs = self.newVMs - self.oldVMs
		return self._outputStructure(alertVMs)

	def _outputStructure(self,vms):
		vr_vm = {}
		for s in self.new:
			for vr in self.new[s]:
				#for vm in self.new[s][vr]['vm_name']:
				dummy = set(self.new[s][vr]['vm_name'])
				i = vms & dummy
				if i:
					if vr not in vr_vm:
						vr_vm[vr] = i
					else:
						vr_vm[vr].update(i)

		return vr_vm
