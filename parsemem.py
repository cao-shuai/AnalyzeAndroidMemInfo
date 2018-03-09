#!/usr/bin/env python
#coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import re
import sys
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from baseparse import BaseParseClass


class MemPareseClass(BaseParseClass):
	"""docstring for ClassName"""
	def __init__(self, path):
		super(MemPareseClass,self).__init__(path);
		self.targetName="result/MemAnalyze/"
		if os.path.exists(self.targetName) is False:
			os.makedirs(self.targetName)

	def ParseFile(self):
		file=open(self.filename);
		for line in file:
			if re.findall(r"^\S+:\s+\d+\s+kB",line):
				#print re.findall(r"^\S+:\s+\d+\s+kB",line);
				strline=re.findall(r"^\S+:\s+\d+\s+kB",line)[0];
				key=re.findall(r"^[a-z,A-Z,_,(,)]+",strline)[0];
				value=int(re.findall(r"\d+",strline)[0])/1024;
				if key in self.tagDirct.keys():
					self.tagDirct[key].append(value);
				else:
					valuelist=[value];
					self.tagDirct[key]=valuelist;
			elif re.findall(r"\S+\s+\S+:\s+\d+\s+kB",line):
				#print re.findall(r"\S+\s+\S+:\s+\d+\s+kB",line);
				strline=re.findall(r"\S+\s+\S+:\s+\d+\s+kB",line)[0];
				key=re.findall(r"[a-z,A-Z]+\s+[a-z,A-Z]+",strline)[0];
				value=int(int(re.findall(r"\d+",strline)[0])/1024);
				if key in self.tagDirct.keys():
					self.tagDirct[key].append(value);
				else:
					valuelist=[value];
					self.tagDirct[key]=valuelist;

		file.close();

	def Draw(self):
		self.__DrawCPUPicutre__();
	
	def __DrawCPUPicutre__(self):
		XtotalLen=[];
		for key in self.tagDirct:
			del XtotalLen[:];
			self.indexPicture=self.indexPicture+1;
			for totallen in xrange(len(self.tagDirct[key])):
				XtotalLen.append(totallen);
			self.plt.figure(self.indexPicture);
			self.plt.plot(XtotalLen,self.tagDirct[key],self.picturesmarklinetyle);
			self.plt.title(key);
			self.plt.xlabel("Times");
			self.plt.ylabel("MB");
			self.plt.savefig(self.targetName+key+".png");