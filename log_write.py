import datetime

class LogWrite:
	def __init__(self,logFile):
		self._logFile = logFile

	def logWrite(self,newVms):
		now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
		with open(self._logFile, 'a') as outfile:
			for vr in newVms:
				for vm in newVms[vr]:
					outfile.write("{0!s} {1!s} is running on the same host where {2!s}\n".format(now,vm,vr))

if __name__ == "__main__":
	pass
