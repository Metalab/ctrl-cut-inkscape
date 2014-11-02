#!/usr/bin/python

import os, sys
from subprocess import call, Popen

def CtrlCut(epsfile):
	call(["ctrl-cut", epsfile])
	os.remove(epsfile)

if __name__ == '__main__':
	if (len(sys.argv) > 2):
		if (sys.argv[2] == "child"):
			CtrlCut(sys.argv[1],)
	else:
		svgfile = sys.argv[-1]
		epsfile = svgfile+".eps"
		null = open(os.devnull, "w")
		call(["inkscape", svgfile, "--export-eps="+epsfile], stderr=null)
		Popen(["python", "ctrl-cut.py", epsfile, "child"], stdout=null, stderr=null)
		null.close()
		os.remove(svgfile)
