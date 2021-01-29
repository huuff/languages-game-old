#!/usr/bin/env sh

file="db"

if [[ "$1" == "--reset" ]]
then
  rm "$file"
elif [[ "$1" == "" ]]
then
  if [ -f "$file" ]
  then
    cat "$file"
  else
    echo ""
  fi
else
  echo "$1" > "$file"
fi
