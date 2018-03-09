#!/usr/bin/env python
#coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import re
import sys
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

class CPUParseClass(object):
	"""docstring for CPUParseClass"""
	def __init__(self, path):
		
		self.filename=path;
		self.targetName="result/CPUAnalyze/";
		if os.path.exists(self.targetName) is False:
			os.makedirs(self.targetName);

		self.plt=plt;
		self.indexPicture=0;
		self.picturesmarklinetyle="-"
		self.tagDirct={};

	def ParseFile(self):
		file=open(self.filename)
		for line in file:
			#define parse cpu useage info string eg: User 11%, System 15%, IOW 0%, IRQ 0%	
			if re.findall(r"\S+\s?\d+%,\s?\S+\s?\d+%,\s?\S+\s?\d+%,",line):
				count=0;
				for index in xrange(len(re.findall(r"\S+\s?\d+%",line))):
					#print re.findall(r"[a-z,A-Z]+\s?\d+%",line)[index];
					strline=re.findall(r"[a-z,A-Z]+\s?\d+%",line)[index];
					key=re.findall(r"[a-z,A-Z]+",strline)[0];
					value=int(re.findall(r"\d+",strline)[0]);
					count=count+value;
					if key in self.tagDirct.keys():
						#be careful value is a string ,and must be switch to int
						self.tagDirct[key].append(value);
					else:
						self.tagDirct[key]=map(int,str(value));
				if "Total CPU Percent" in self.tagDirct.keys():
					self.tagDirct["Total CPU Percent"].append(count);
				else:
					self.tagDirct["Total CPU Percent"]=map(int,str(count));
			else:
				pass
				#need instance
		file.close();

	def Draw(self):
		self.__DrawCPUPicutre__();
		self.__DrawSUMImportantInfoPicture__();

	def __DrawCPUPicutre__(self):
		XtotalLen=[];
		for key in self.tagDirct:
			del XtotalLen[:];
			self.indexPicture=self.indexPicture+1;
			for totallen in xrange(len(self.tagDirct[key])):
				XtotalLen.append(totallen);
			self.plt.figure(self.indexPicture);
			self.plt.plot(XtotalLen,self.tagDirct[key],self.picturesmarklinetyle);
			self.plt.title(key+" CPU Percent");
			self.plt.xlabel("Times");
			self.plt.ylabel("Percent");
			self.plt.savefig(self.targetName+key+" Percent.png");


	def __DrawSUMImportantInfoPicture__(self):
		namelist=[];
		valuelist=[];
		if "Total CPU Percent" in self.tagDirct.keys():
			MaximumCPUPercent=self.__GetMaxVaule__(self.tagDirct["Total CPU Percent"]);
			namelist.append('MaximumCPUPercent');
			valuelist.append(MaximumCPUPercent);
			AverageCPUPercent=self.__GetAverageValue__(self.tagDirct["Total CPU Percent"]);
			namelist.append('AverageCPUPercent');
			valuelist.append(AverageCPUPercent);
			self.indexPicture=self.indexPicture+1;
			self.plt.figure(self.indexPicture);
			self.plt.bar(range(len(valuelist)),valuelist,color='rgb',tick_label=namelist);
			self.plt.savefig(self.targetName+"SUMImportantInfo Percent.png");

	def __GetMaxVaule__(self,value):
		maxvalue=0;
		for index in xrange(len(value)):
			if value[index] > maxvalue:
				maxvalue=value[index];
		return maxvalue;

	def __GetAverageValue__(self,value):
		total=0;
		if len(value) == 0:
			return Total;
		for index in xrange(len(value)):
			total=total+value[index];
		return total/len(value);