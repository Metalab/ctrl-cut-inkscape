#!/usr/bin/python

import os, sys
from subprocess import call

svgfile = sys.argv[-1]
epsfile = svgfile+".eps"
null = open(os.devnull, "w")
call(["inkscape", svgfile, "--export-eps="+epsfile], stderr=null)
call(["ctrl-cut", epsfile], stderr=null)
null.close()
os.remove(svgfile)
os.remove(epsfile)
