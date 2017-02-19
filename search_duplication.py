class SearchDuplication():
	def __init__(self,old,new):
		self.newVMs = set()
		self.oldVMs = set()
		self.old = old
		self.new = new


	def createSetOfNewVms(self):
		new = self.new
		for i in new:
			for m in new[i]:
				self.newVMs.update(new[i][m]['vm_name'])


	def createSetOfOldVms(self):
		old = self.old
		for i in old:
			for m in old[i]:
				self.oldVMs.update(old[i][m]['vm_name'])


	def searchNewVMs(self):
		self.createSetOfNewVms()
		self.createSetOfOldVms()
		alertVMs = self.newVMs - self.oldVMs
		print(alertVMs)

