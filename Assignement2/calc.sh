# read variables from the command line, one by one:

option=$1; # load command-line arg into option
shift;     # eat currently first command-line arg
if [ $# -lt 1 ]; then
	echo "error too few arguments, minimum 2: type number"
	exit
fi
if [ "$option" == "S" ]; then
	
    	#S+=$1; shift;
	while [ $# -gt 0 ]
	do 
		((S+=$1)); shift;
	done
elif [ "$option" == "P" ]; then
P=1
    	while [ $# -gt 0 ]
	do 
		((P*=$1)); shift;
	done;
elif [ "$option" == "M" ]; then
	x=0;
	while [ $# -gt 0 ]
	do 
		if [ $x -lt $1 ]; then
			((x=$1)); shift;
		else
			shift;
		fi
	M=$x
	done
elif [ "$option" == "m" ]; then
    	x=$((2**32)); #32 bit max?
	while [ $# -gt 0 ]
	do 
		if [ $x -gt $1 ]; then
			((x=$1)); shift;
		else
			shift;
		fi
	m=$x
	done
else
    	echo exit;
fi


echo "Command line arguments:"
[ -n "$S" ] && echo "S=$S"
[ -n "$P" ] && echo "P=$P"
[ -n "$M" ] && echo "M=$M"
[ -n "$m" ] && echo "m=$m"
