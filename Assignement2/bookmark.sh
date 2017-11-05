#!/bin/bash


if [ $# -lt 1 ]; then
	filename="$HOME/.bookmarks"
	while read -r line
	do
		name="$line"
		echo "Name read from file - $name"
		value=${name##*|}
		varname=${name%"|"$value}
		export $varname="$value"
	done < "$filename"
fi
if [ $# -gt 0 ]; then
	option=$1;
	shift;
    	if [ "$option" == "-a" ]; then
    		bookmarkname=$1; shift; 
		bookmarklocation=$PWD
		echo "$bookmarkname|$bookmarklocation" >> /$HOME/.bookmarks
		
	elif [ "$option" == "-r" ]; then
		tmp=$1; 
		filename="$HOME/.bookmarks"
		touch /$HOME/outfile
		while read -r line
		do
			name="$line"
			#echo "Name read from file - $name"
			value=${name##*|}
			varname=${name%"|"$value}
			if [ $tmp != $varname ]; then
				echo "$varname|$value" >> /$HOME/outfile
			fi
		done < "$filename"
		rm -f "$HOME/.bookmarks"
		mv $HOME/outfile $HOME/.bookmarks
		rm -f outfile
	else
    		echo "error: invalid arguments";
	fi
fi







# echo |-separated list bookmarkname|bookmarklocation
