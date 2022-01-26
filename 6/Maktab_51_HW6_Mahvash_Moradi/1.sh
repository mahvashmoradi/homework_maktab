#! /bin/bash
mkdir ~/music_box
find ~ -type f -iname "*.mp3" -print -exec cp {} ~/music_box \; | sort
ls ~/music_box > ~/music_list.txt
rdfind -deleteduplicates true ~/music_box
export GZIP=-9
tar cvzf file.tar.gz ~/music_box
