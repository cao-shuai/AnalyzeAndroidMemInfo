# AnalyzeAndroidMemInfo
利用脚本分析长期抓取的mem信息生成对应的mem图表信息，主要用来判断mem的整体走势

1. 环境配置：
   a) linux 环境配置(可以有所不同)：
   Linux version 3.16.0-30-generic (buildd@kissel) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #40~14.04.1-Ubuntu SMP Thu Jan 15 17:43:14 UTC 2015
   b) python version:
   	  Python 2.7.6 (default, Mar 22 2014, 22:59:56)
   c) python 插件： matplotlib：配置方法见： https://matplotlib.org/ 

2. 使用说明:
   a) 把memdebug.sh copy 到/data/目录下：然后切换到/data工作目录下执行
   sh memdebug.sh > /mnt/usb/sda1/meminfo.log & 

   b) 抓到的对应的meminfo.log信息，使用python parsemem.py meminfo.log 即可在同一级目录result/目录下生成对应的png图片


