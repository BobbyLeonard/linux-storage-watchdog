#!/usr/bin/python3

from datetime import datetime
from subprocess import check_output
from subprocess import run
from time import sleep


# Edit these to suit !
dirToWatch='/home/bobby/storage'
dirKByteLimit=10000
# 50GB = 50000000

logFile='/tmp/storageWatchdog.log'
ASCtimeSortedSubDirs=[]

def writeLogs(stringToWrite):
	with open(logFile,'a+') as f: 
		f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n" + stringToWrite + "\n\n") 

def getDirSize():
	command='du -s {}'.format(dirToWatch)
	commandSplitList=[x for x in command.split()]
	output=check_output(commandSplitList)
	KByteSizeOfDir=output.decode("utf-8").split()[0]
	return int(KByteSizeOfDir)

def getSubDirsInDir():
	command='ls -lthr {}'.format(dirToWatch)
	commandSplitList=[x for x in command.split()]
	output=check_output(commandSplitList)
	dirContains=output.decode("utf-8").split('\n')
	ASCtimeSortedSubDirs=[]
	for subDir in dirContains[1:-1]:
		ASCtimeSortedSubDirs.append(subDir.split()[-1])	
	return ASCtimeSortedSubDirs	

while True:
	KByteSizeOfDir=getDirSize()
	if int(KByteSizeOfDir) > dirKByteLimit:
		try:
			ASCtimeSortedSubDirs=getSubDirsInDir()
			command='rm -rf {}/{}'.format(dirToWatch, ASCtimeSortedSubDirs[0])
			commandSplitList=[x for x in command.split()]
			output=run(commandSplitList)
			writeLogs(command)
			KByteSizeOfDir=getDirSize()
		except Exception as e:
			writeLogs(str(e))
			continue
	else:
		try:
			sleep(10)
		except Exception as e:
			writeLogs(str(e))
			continue
