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
		self.UserCPU=[];
		self.SystemCPU=[];
		self.IOWCPU=[];
		self.IRQCPU=[];
		self.totalCPU=[];
		self.XtotalLen=[];

		self.filename=path;
		self.targetName="result/CPUAnalyze/";
		if os.path.exists(self.targetName) is False:
			os.makedirs(self.targetName);

		self.picturesmarklinetyle="-"

	def ParseFile(self):
		file=open(self.filename)
		index=0;
		for line in file:
			if re.findall(r"\S+\s?\d+%,\s?\S+\s?\d+%,\s?\S+\s?\d+%,",line):
				self.XtotalLen.append(index);
				index=index+1;
				count=0;
				Userline=re.findall(r"User \d+%",line)[0];
				#print "User: "+re.findall(r"\d+",Userline)[0];
				count=count+int(re.findall(r"\d+",Userline)[0]);
				self.UserCPU.append(int(re.findall(r"\d+",Userline)[0]));

				Systemline=re.findall(r"System \d+%",line)[0];
				#print "system: "+re.findall(r"\d+",Systemline)[0];
				count=count+int(re.findall(r"\d+",Systemline)[0]);
				self.SystemCPU.append(int(re.findall(r"\d+",Systemline)[0]))
				
				IOWline=re.findall(r"IOW \d+%",line)[0];
				#print "IOW: "+re.findall(r"\d+",IOWline)[0];
				count=count+int(re.findall(r"\d+",IOWline)[0]);
				self.IOWCPU.append(int(re.findall(r"\d+",IOWline)[0]))
				
				IRQline=re.findall(r"IRQ \d+%",line)[0];
				#print "IRQ: "+re.findall(r"\d+",IRQline)[0];
				count=count+int(re.findall(r"\d+",IRQline)[0]);
				self.IRQCPU.append(int(re.findall(r"\d+",IRQline)[0]))
				print "toal cpu percent is: %s%%"%(count);
				self.totalCPU.append(count);
		file.close();

	def Draw(self):
		self.plt=plt;
		self.__DrawTotalCPU__(1);
		self.__DrawUserCPU__(2);
		self.__DrawSystemCPU__(3);
		self.__DrawIRQCPU__(4);
		self.__DrawIOWCPU__(5);

	def __DrawTotalCPU__(self,ind):
		maxvalue=self.__GetMaxVaule__(self.totalCPU);
		print "toal cpu letter percent is: %s%%"%(maxvalue);
		avergevalue=self.__GetAverageValue__(self.totalCPU);
		print "toal cpu average percent is: %s%%"%(avergevalue);
		self.plt.figure(ind);
		self.plt.plot(self.XtotalLen,self.totalCPU,self.picturesmarklinetyle);
		self.plt.title("Total CPU percent");
		self.plt.xlabel("times");
		self.plt.ylabel("Percent");
		self.plt.savefig(self.targetName+"Total CPU Percent.png");


	def __DrawUserCPU__(self,ind):
		self.plt.figure(ind);
		self.plt.plot(self.XtotalLen,self.UserCPU,self.picturesmarklinetyle);
		self.plt.title("User CPU percent");
		self.plt.xlabel("times");
		self.plt.ylabel("Percent");
		self.plt.savefig(self.targetName+"User CPU Percent.png");

	def __DrawSystemCPU__(self,ind):
		self.plt.figure(ind);
		self.plt.plot(self.XtotalLen,self.SystemCPU,self.picturesmarklinetyle);
		self.plt.title("System CPU percent");
		self.plt.xlabel("times");
		self.plt.ylabel("Percent");
		self.plt.savefig(self.targetName+"System CPU Percent.png");

	def __DrawIOWCPU__(self,ind):
		self.plt.figure(ind);
		self.plt.plot(self.XtotalLen,self.IOWCPU,self.picturesmarklinetyle);
		self.plt.title("IOW CPU percent");
		self.plt.xlabel("times");
		self.plt.ylabel("Percent");
		self.plt.savefig(self.targetName+"IOW CPU Percent.png");

	def __DrawIRQCPU__(self,ind):
		self.plt.figure(ind);
		self.plt.plot(self.XtotalLen,self.IRQCPU,self.picturesmarklinetyle);
		self.plt.title("IRQ CPU percent");
		self.plt.xlabel("times");
		self.plt.ylabel("Percent");
		self.plt.savefig(self.targetName+"IRQ CPU Percent.png");

	def __GetMaxVaule__(self,value):
		maxvalue=0;
		for index in xrange(len(value)):
			if value[index] > maxvalue:
				maxvalue=value[index];
		return maxvalue;

	def __GetAverageValue__(self,value):
		total=0;
		for index in xrange(len(value)):
			total=total+value[index];
		return total/len(value);


if __name__ == '__main__':
	CPUparse=CPUParseClass(sys.argv[1]);
	CPUparse.ParseFile();
	CPUparse.Draw();
			
		
