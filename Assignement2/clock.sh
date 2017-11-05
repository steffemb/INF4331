#!/bin/bash


option=$1;
if [ "$option" == "us" ]; then
	while [ 1 ]
	do
		clear
		TZ=America/New_York date
		
		sleep 1
	done
fi
if [ "$option" == "sk" ]; then
	while [ 1 ]
	do
		clear
		TZ=Asia/Seoul date
		
		sleep 1
	done
fi
if [ "$option" == "no" ]; then
	while [ 1 ]
	do
		clear
		TZ=Europe/Oslo date
		
		sleep 1
	done
fi
echo "invalid arguments (no us sk)"
exit
