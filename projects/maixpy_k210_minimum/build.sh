#!/bin/bash

cmd=$1

case $cmd in
	build)
	  python3 project.py build
	  ;;
	menuconfig)
	  python3 project.py menuconfig
	  ;;
	clean)
	  python3 project.py distclean
	  ;;
	flash)
	  python3 project.py -B bananapi -p /dev/ttyUSB0 -b 1500000 -t -S flash
	  ;;
	*)
	  echo "invalid command"
esac

echo "finish"
