while [[ 1 ]]; do
	#statements
	echo "================================================================"
	cat /proc/meminfo;
	cat /sys/kernel/debug/mali/gpu_memory;
	dumpsys meminfo;
	sleep 30
done
