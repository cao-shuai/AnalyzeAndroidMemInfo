#!/usr/bin/env python
#coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import re
import sys
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter  


class MemPareseClass(object):
	"""docstring for ClassName"""
	def __init__(self, path):
		self.FreeRAM=[];
		self.LostRAM=[];
		self.UsedRAM=[];
		self.ZRAM=[];
		self.MaliMemusage=[];
		self.picturesmarklinetyle="-"

		self.MemFree=[];
		self.Buffers=[];
		self.Cached=[];
		self.SwapCached=[];
		self.Active=[];
		self.Inactive=[];
		self.Active_anon=[];
		self.Inactive_anon=[];
		self.Active_file=[];
		self.Inactive_file=[];
		self.Unevictable=[];
		self.Mlocked=[];
		self.HighTotal=[];
		self.HighFree=[];
		self.LowTotal=[];
		self.LowFree=[];
		self.SwapTotal=[];
		self.SwapFree=[];
		self.Dirty=[];
		self.Writeback=[];
		self.AnonPages=[];
		self.Mapped=[];
		self.Shmem=[];
		self.Slab=[];
		self.SReclaimable=[];
		self.SUnreclaim=[];
		self.KernelStack=[];
		self.PageTables=[];
		self.NFS_Unstable=[];
		self.Bounce=[];
		self.WritebackTmp=[];
		self.CommitLimit=[];
		self.Committed_AS=[];
		self.VmallocTotal=[];
		self.VmallocUsed=[];
		self.VmallocChunk=[];
		self.CMAFree=[]; 
		self.Native=[];

		self.filename=path;

		if os.path.exists("reslut/") is False:
			os.makedirs("reslut/")

	def ParseFile(self):
		file=open(self.filename);
		for line in file:
			if re.match(r'[\s]?Free RAM:',line) is not None and re.findall(r"\d+",line) is not None:
				self.FreeRAM.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'[\s]?Used RAM:',line) is not None and re.findall(r"\d+",line) is not None:
				self.UsedRAM.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'[\s]?Lost RAM:',line) is not None and re.findall(r"\d+",line) is not None:
				self.LostRAM.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'[\s]?ZRAM:',line) is not None and re.findall(r"\d+",line) is not None:
				self.ZRAM.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'[\s]?Mali mem usage:',line) is not None and re.findall(r"\d+",line) is not None:
				self.MaliMemusage.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^MemFree:',line) is not None and re.findall(r"\d+",line) is not None:
				self.MemFree.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Buffers:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Buffers.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Cached:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Cached.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^SwapCached:',line) is not None and re.findall(r"\d+",line) is not None:
				self.SwapCached.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Active:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Active.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Inactive:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Inactive.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Active\(anon\):',line) is not None and re.findall(r"\d+",line) is not None:
				self.Active_anon.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Inactive\(anon\):',line) is not None and re.findall(r"\d+",line) is not None:
				self.Inactive_anon.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Active\(file\):',line) is not None and re.findall(r"\d+",line) is not None:
				self.Active_file.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Inactive\(file\):',line) is not None and re.findall(r"\d+",line) is not None:
				self.Inactive_file.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Unevictable:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Unevictable.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Mlocked:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Mlocked.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^HighTotal:',line) is not None and re.findall(r"\d+",line) is not None:
				self.HighTotal.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^HighFree:',line) is not None and re.findall(r"\d+",line) is not None:
				self.HighFree.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^LowTotal:',line) is not None and re.findall(r"\d+",line) is not None:
				self.LowTotal.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^LowFree:',line) is not None and re.findall(r"\d+",line) is not None:
				self.LowFree.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^SwapTotal:',line) is not None and re.findall(r"\d+",line) is not None:
				self.SwapTotal.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^SwapFree:',line) is not None and re.findall(r"\d+",line) is not None:
				self.SwapFree.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Dirty:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Dirty.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Writeback:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Writeback.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^AnonPages:',line) is not None and re.findall(r"\d+",line) is not None:
				self.AnonPages.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Mapped:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Mapped.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Shmem:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Shmem.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Slab:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Slab.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^SReclaimable:',line) is not None and re.findall(r"\d+",line) is not None:
				self.SReclaimable.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^SUnreclaim:',line) is not None and re.findall(r"\d+",line) is not None:
				self.SUnreclaim.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^KernelStack:',line) is not None and re.findall(r"\d+",line) is not None:
				self.KernelStack.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^PageTables:',line) is not None and re.findall(r"\d+",line) is not None:
				self.PageTables.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^NFS_Unstable:',line) is not None and re.findall(r"\d+",line) is not None:
				self.NFS_Unstable.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Bounce:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Bounce.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^WritebackTmp:',line) is not None and re.findall(r"\d+",line) is not None:
				self.WritebackTmp.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^CommitLimit:',line) is not None and re.findall(r"\d+",line) is not None:
				self.CommitLimit.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^Committed_AS:',line) is not None and re.findall(r"\d+",line) is not None:
				self.Committed_AS.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^VmallocTotal:',line) is not None and re.findall(r"\d+",line) is not None:
				self.VmallocTotal.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^VmallocUsed:',line) is not None and re.findall(r"\d+",line) is not None:
				self.VmallocUsed.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^VmallocChunk:',line) is not None and re.findall(r"\d+",line) is not None:
				self.VmallocChunk.append((int(re.findall(r"\d+",line)[0]))/1024);
			elif re.match(r'^CMA Free:',line) is not None and re.findall(r"\d+",line) is not None:
				self.CMAFree.append((int(re.findall(r"\d+",line)[0]))/1024);
		file.close();

	def Draw(self):
		self.plt=plt;
		self.__DrawFreeRAM__(1);
		self.__DrawUsedRAM__(2);
		self.__DrawLostRAM__(3);
		self.__MaliMemUsage__(4);
		self.__DrawMemInfoMemFreeRAM__(5);
		self.__DrawMemInfoBuffersRAM__(6);
		self.__DrawMemInfoCachedRAM__(7);
		self.__DrawMemInfoSwapCachedRAM__(8);
		self.__DrawMemInfoActiveRAM__(9);
		self.__DrawMemInfoInactiveRAM__(10);
		self.__DrawMemInfoActive_anonRAM__(11);
		self.__DrawMemInfoInactive_anonRAM__(12);
		self.__DrawMemInfoActive_fileRAM__(13);
		self.__DrawMemInfoInactive_fileRAM__(14);
		self.__DrawMemInfoUnevictableRAM__(15);
		self.__DrawMemInfoMlockedRAM__(16);
		self.__DrawMemInfoHighTotalRAM__(17);
		self.__DrawMemInfoHighFreeRAM__(18);
		self.__DrawMemInfoLowTotalRAM__(19);
		self.__DrawMemInfoLowFreeRAM__(20);
		self.__DrawMemInfoSwapTotalRAM__(21);
		self.__DrawMemInfoSwapFreeRAM__(22);
		self.__DrawMemInfoDirtyRAM__(23);
		self.__DrawMemInfoWritebackRAM__(24);
		self.__DrawMemInfoAnonPagesRAM__(25);
		self.__DrawMemInfoMappedRAM__(26);
		self.__DrawMemInfoShmemRAM__(27);
		self.__DrawMemInfoSlabRAM__(28);
		self.__DrawMemInfoSReclaimableRAM__(29);
		self.__DrawMemInfoSUnreclaimRAM__(30);
		self.__DrawMemInfoKernelStackRAM__(31);
		self.__DrawMemInfoPageTablesRAM__(32);
		self.__DrawMemInfoNFS_UnstableRAM__(33);
		self.__DrawMemInfoBounceRAM__(34);
		self.__DrawMemInfoWritebackTmpRAM__(35);
		self.__DrawMemInfoCommitLimitRAM__(36);
		self.__DrawMemInfoCommitted_ASRAM__(37);
		self.__DrawMemInfoVmallocTotalRAM__(38);
		self.__DrawMemInfoVmallocUsedRAM__(39);
		self.__DrawMemInfoVmallocChunkRAM__(40);
		self.__DrawMemInfoCMAFreeRAM__(41);
		#self.plt.show();

	def __DrawMemInfoMemFreeRAM__(self,ind):
		x=[];
		for index in xrange(len(self.MemFree)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.MemFree,self.picturesmarklinetyle);
		self.plt.title("MemFree");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/MemFree.png")

	def __DrawMemInfoBuffersRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Buffers)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Buffers,self.picturesmarklinetyle);
		self.plt.title("Buffers");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Buffers.png");

	def __DrawMemInfoCachedRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Cached)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Cached,self.picturesmarklinetyle);
		self.plt.title("Cached");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Cached.png");

	def __DrawMemInfoSwapCachedRAM__(self,ind):
		x=[];
		for index in xrange(len(self.SwapCached)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.SwapCached,self.picturesmarklinetyle);
		self.plt.title("SwapCached");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/SwapCached.png");

	def __DrawMemInfoActiveRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Active)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Active,self.picturesmarklinetyle);
		self.plt.title("Active");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Active.png");

	def __DrawMemInfoInactiveRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Inactive)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Inactive,self.picturesmarklinetyle);
		self.plt.title("Inactive");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Inactive.png");

	def __DrawMemInfoActive_anonRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Active_anon)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Active_anon,self.picturesmarklinetyle);
		self.plt.title("Active(anon)");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Active_anon.png");

	def __DrawMemInfoInactive_anonRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Inactive_anon)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Inactive_anon,self.picturesmarklinetyle);
		self.plt.title("Inactive(anon)");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Inactive_anon.png");

	def __DrawMemInfoActive_fileRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Active_file)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Active_file,self.picturesmarklinetyle);
		self.plt.title("Active(file)");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Active_file.png");

	def __DrawMemInfoInactive_fileRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Inactive_file)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Inactive_file,self.picturesmarklinetyle);
		self.plt.title("Inactive(file)");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Inactive_file.png");

	def __DrawMemInfoUnevictableRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Unevictable)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Unevictable,self.picturesmarklinetyle);
		self.plt.title("Unevictable");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Unevictable.png");

	def __DrawMemInfoMlockedRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Mlocked)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Mlocked,self.picturesmarklinetyle);
		self.plt.title("Mlocked");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Mlocked.png");

	def __DrawMemInfoHighTotalRAM__(self,ind):
		x=[];
		for index in xrange(len(self.HighTotal)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.HighTotal,self.picturesmarklinetyle);
		self.plt.title("HighTotal");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/HighTotal.png");

	def __DrawMemInfoHighFreeRAM__(self,ind):
		x=[];
		for index in xrange(len(self.HighFree)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.HighFree,self.picturesmarklinetyle);
		self.plt.title("HighFree");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/HighFree.png");

	def __DrawMemInfoLowTotalRAM__(self,ind):
		x=[];
		for index in xrange(len(self.LowTotal)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.LowTotal,self.picturesmarklinetyle);
		self.plt.title("LowTotal");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/LowTotal.png");

	def __DrawMemInfoLowFreeRAM__(self,ind):
		x=[];
		for index in xrange(len(self.LowFree)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.LowFree,self.picturesmarklinetyle);
		self.plt.title("LowFree");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/LowFree.png");

	def __DrawMemInfoSwapTotalRAM__(self,ind):
		x=[];
		for index in xrange(len(self.SwapTotal)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.SwapTotal,self.picturesmarklinetyle);
		self.plt.title("SwapTotal");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/SwapTotal.png");

	def __DrawMemInfoSwapFreeRAM__(self,ind):
		x=[];
		for index in xrange(len(self.SwapFree)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.SwapFree,self.picturesmarklinetyle);
		self.plt.title("SwapFree");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/SwapFree.png");

	def __DrawMemInfoDirtyRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Dirty)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Dirty,self.picturesmarklinetyle);
		self.plt.title("Dirty");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Dirty.png");

	def __DrawMemInfoWritebackRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Writeback)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Writeback,self.picturesmarklinetyle);
		self.plt.title("Writeback");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Writeback.png");

	def __DrawMemInfoAnonPagesRAM__(self,ind):
		x=[];
		for index in xrange(len(self.AnonPages)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.AnonPages,self.picturesmarklinetyle);
		self.plt.title("AnonPages");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/AnonPages.png");

	def __DrawMemInfoMappedRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Mapped)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Mapped,self.picturesmarklinetyle);
		self.plt.title("Mapped");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Mapped.png");

	def __DrawMemInfoShmemRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Shmem)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Shmem,self.picturesmarklinetyle);
		self.plt.title("Shmem");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Shmem.png");

	def __DrawMemInfoSlabRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Slab)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Slab,self.picturesmarklinetyle);
		self.plt.title("Slab");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Slab.png");

	def __DrawMemInfoSReclaimableRAM__(self,ind):
		x=[];
		for index in xrange(len(self.SReclaimable)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.SReclaimable,self.picturesmarklinetyle);
		self.plt.title("SReclaimable");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/SReclaimable.png");

	def __DrawMemInfoSUnreclaimRAM__(self,ind):
		x=[];
		for index in xrange(len(self.SUnreclaim)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.SUnreclaim,self.picturesmarklinetyle);
		self.plt.title("SUnreclaim");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/SUnreclaim.png");

	def __DrawMemInfoKernelStackRAM__(self,ind):
		x=[];
		for index in xrange(len(self.KernelStack)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.KernelStack,self.picturesmarklinetyle);
		self.plt.title("KernelStack");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/KernelStack.png");

	def __DrawMemInfoPageTablesRAM__(self,ind):
		x=[];
		for index in xrange(len(self.PageTables)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.PageTables,self.picturesmarklinetyle);
		self.plt.title("PageTables");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/PageTables.png");

	def __DrawMemInfoNFS_UnstableRAM__(self,ind):
		x=[];
		for index in xrange(len(self.NFS_Unstable)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.NFS_Unstable,self.picturesmarklinetyle);
		self.plt.title("NFS_Unstable");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/NFS_Unstable.png");

	def __DrawMemInfoBounceRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Bounce)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Bounce,self.picturesmarklinetyle);
		self.plt.title("Bounce");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Bounce.png");

	def __DrawMemInfoWritebackTmpRAM__(self,ind):
		x=[];
		for index in xrange(len(self.WritebackTmp)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.WritebackTmp,self.picturesmarklinetyle);
		self.plt.title("WritebackTmp");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/WritebackTmp.png");

	def __DrawMemInfoCommitLimitRAM__(self,ind):
		x=[];
		for index in xrange(len(self.CommitLimit)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.CommitLimit,self.picturesmarklinetyle);
		self.plt.title("CommitLimit");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/CommitLimit.png");

	def __DrawMemInfoCommitted_ASRAM__(self,ind):
		x=[];
		for index in xrange(len(self.Committed_AS)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.Committed_AS,self.picturesmarklinetyle);
		self.plt.title("Committed_AS");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Committed_AS.png");

	def __DrawMemInfoVmallocTotalRAM__(self,ind):
		x=[];
		for index in xrange(len(self.VmallocTotal)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.VmallocTotal,self.picturesmarklinetyle);
		self.plt.title("VmallocTotal");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/VmallocTotal.png");

	def __DrawMemInfoVmallocUsedRAM__(self,ind):
		x=[];
		for index in xrange(len(self.VmallocUsed)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.VmallocUsed,self.picturesmarklinetyle);
		self.plt.title("VmallocUsed");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/VmallocUsed.png");

	def __DrawMemInfoVmallocChunkRAM__(self,ind):
		x=[];
		for index in xrange(len(self.VmallocChunk)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.VmallocChunk,self.picturesmarklinetyle);
		self.plt.title("VmallocChunk");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/VmallocChunk.png");

	def __DrawMemInfoCMAFreeRAM__(self,ind):
		x=[];
		for index in xrange(len(self.CMAFree)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.CMAFree,self.picturesmarklinetyle);
		self.plt.title("CMA Free");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/CMA_Free.png");

	def __DrawFreeRAM__(self,ind):
		x=[];
		for index in xrange(len(self.FreeRAM)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.FreeRAM,self.picturesmarklinetyle);
		self.plt.title("Free RAM");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Free_RAM.png");

	def __DrawUsedRAM__(self,ind):
		x=[];
		for index in xrange(len(self.UsedRAM)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.UsedRAM,self.picturesmarklinetyle);
		self.plt.title("UsedRAM");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/UsedRAM.png");

	def __DrawLostRAM__(self,ind):
		x=[];
		for index in xrange(len(self.LostRAM)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.LostRAM,self.picturesmarklinetyle);
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.title("LostRAM");
		self.plt.savefig("reslut/LostRAM.png");

	def __MaliMemUsage__(self,ind):
		x=[];
		for index in xrange(len(self.MaliMemusage)):
			x.append(index);
		self.plt.figure(ind);
		self.plt.plot(x,self.MaliMemusage,self.picturesmarklinetyle);
		self.plt.title("Mali mem usage");
		self.plt.xlabel("times");
		self.plt.ylabel("MB");
		self.plt.savefig("reslut/Mali-mem-usage.png");

if __name__=="__main__":
	mempaser=MemPareseClass(sys.argv[1]);
	mempaser.ParseFile();
	mempaser.Draw();