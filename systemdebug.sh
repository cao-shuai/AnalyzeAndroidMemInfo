function GetMEMINFO(){
	while [[ 1 ]]; do
		#statements
		echo "================================================================";
		cat /proc/meminfo;
		cat /sys/kernel/debug/mali/gpu_memory;
		dumpsys meminfo;
		sleep 30;
	done
}

function GETCPUINFO(){
	while [[ 1 ]]; do
		#statements
		echo "================================================================";
		#cat /proc/cpuinfo;
		echo "cpu hotplug open core:"
		cat /proc/cpuinfo |grep "processor" | grep -Eo "[0-9]" | busybox wc -l
		echo "top 10 process: "
		top -m 10 -n 1;
		sleep 1
	done
}

function HELP(){
	echo "===================================================================">/dev/ttyS0;
	echo "./debug.sh mem : dump mem info to file and store it for analyze!!!">/dev/ttyS0
	echo "./debug.sh cpu : dump cpu info to file and store it for analyze!!!">/dev/ttyS0;
	echo "please input right commandline ">/dev/ttyS0
	echo "===================================================================">/dev/ttyS0;
}

if [[ $1 == "mem" ]]; then
	#statements
	GetMEMINFO;
elif [[ $1 == "cpu" ]]; then
	#statements
	GETCPUINFO;
else
	HELP;
fi