#! /bin/bash
file="name.txt"
name=$(cat "$file")
echo $name
for TOKEN in $name
do
mkdir -m+7 $TOKEN
echo "Student name: $TOKEN " > $TOKEN/$TOKEN-info.txt
done


