#!/usr/bin/python

import inkex, os, sys
from subprocess import call

class CtrlCut(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)

	def effect(self):
		svgfile = sys.argv[-1]
		epsfile = svgfile+".eps"
		null = open(os.devnull, "w")
		call(["inkscape", svgfile, "--export-eps="+epsfile], stderr=null)
		call(["ctrl-cut", epsfile], stderr=null)
		null.close()
		os.remove(svgfile)
		os.remove(epsfile)

if __name__ == '__main__':
	effect = CtrlCut()
	effect.affect()
