#!/usr/bin/env python
#coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import re
import sys
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

class BaseParseClass(object):
	"""docstring for BaseParseClass"""
	def __init__(self, path):
		self.filename=path;
		self.plt=plt;
		self.indexPicture=0;
		self.picturesmarklinetyle="-"
		self.tagDirct={};
		self.targetName="";

	def ParseFile(self):
		pass

	def Draw(self):
		pass

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