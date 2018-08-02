#!/usr/bin/env python
#coding: utf-8
import sys
from parsemem import MemPareseClass
from parsecpu import CPUParseClass

if __name__ == '__main__':
	comadlenth=len(sys.argv);
	if comadlenth ==3:
		parse=None
		comandline=sys.argv[1];
		if "CPU" in comandline or "cpu" in comandline :
			parse=CPUParseClass(sys.argv[2]);
		elif "MEM" in comandline or "mem" in comandline:
			parse=MemPareseClass(sys.argv[2]);
		if parse is not None:
			parse.ParseFile();
			parse.Draw();
	else:
		print "======================================================================================";
		print "--CPU filename OR --cpu filename: parse cpu info to pictures";
		print "--MEM filename OR --mem filename: parse mem info to pictures";
		print "other commad will be support later";
		print "======================================================================================";
		