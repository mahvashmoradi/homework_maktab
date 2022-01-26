#! /bin/bash
for TOKEN in $*
do
mkdir -m+7 $TOKEN
echo "Student name: $TOKEN " > $TOKEN-info.txt
done
