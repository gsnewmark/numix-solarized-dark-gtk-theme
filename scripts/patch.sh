#!/bin/bash

action=$1
theme=$2

case $action in
	clean)
		find . -name *.in | sed 's/\.in$//' | xargs rm -f
		;;
	patch)
		find . -name *.in | sed 's/\(.*\)\.in$/\1.in \1/' | xargs -l scripts/colors.py "$theme"
		;;
esac
