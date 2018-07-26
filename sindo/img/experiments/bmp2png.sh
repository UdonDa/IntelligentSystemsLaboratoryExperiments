#!/bin/sh
for f in $(ls *.bmp)
do
  f2=`echo $f | sed -e "s/bmp$/png/"`
  convert $f $f2
done
