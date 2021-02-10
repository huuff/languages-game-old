#!/usr/bin/env sh

file="db"

if [[ "$1" == "--reset" ]]
then
  rm "$file"
  exit
fi

if [[ -f "$file" ]]
then
  key_string="^$1:"
  contents=`cat "$file" | grep "$key_string"`
fi

if [[ "$2" == "" ]]
then
  echo "$contents" | cut -d ':' -f 2
else
  if [[ "$contents" != "" ]]
  then
    sed -i "/^$1:.*/d" "$file"
  fi
  echo "$1:$2" >> "$file"
fi
