#!/bin/bash
cd my-python-project
echo "(a) Number of python files: " $(git ls-files "./*.py" | wc -l)
echo "(b)" 
npm install cloc --quiet
cloc . 
cd ~/
echo "(c) Number of functions: " $(python3 ~/q5c.py) 
cd my-python-project
echo "(d) Number of lines of change: " $(git diff HEAD HEAD~3 | wc -l)
echo "(e) Total folder size in MB:" 
du -d 2 -m ~/my-python-project | sort -n | awk '{printf "%.3f MB %s\n", $1/1024, $2}'
