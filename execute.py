# code for executing mis_pred for different selectivity set.

import sys
import subprocess

print "The query file name: "+sys.argv[1]


params = []
with open(sys.argv[1], "r") as file:
	params = []
	for line in file:
		l = line.split()
		#params.append([float(i) for i in l])
		params.append(l)

print params;

for i in range(0,11):
	print "==============================================================="
	print "The", i,"th execution, params:", params[i] 
	process = subprocess.Popen(["./branch_mispred", params[i][0], params[i][1], params[i][2], params[i][3]], stdout=subprocess.PIPE);
	while True:
  		line = process.stdout.readline()
  		if line != '':
    			print line
  		else:
    			break
