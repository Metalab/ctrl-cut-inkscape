#!/usr/bin/python

import os, sys
from subprocess import call, Popen

def CtrlCut(epsfile):
	call(["ctrl-cut", epsfile])
	os.remove(epsfile)

if __name__ == '__main__':
	if (sys.argv[1] == "child"):
		CtrlCut(sys.argv[2],)
	else:
		svgfile = sys.argv[-1]
		epsfile = svgfile+".eps"
		null = open(os.devnull, "w")
		call(["inkscape", svgfile, "--export-eps="+epsfile], stderr=null)
		if sys.platform == "win32":
			Popen(["pythonw", "ctrl-cut.py", "child", epsfile], close_fds=True)
		else:
			Popen(["python", "ctrl-cut.py", "child", epsfile], stdout=null, stderr=null)
		null.close()
