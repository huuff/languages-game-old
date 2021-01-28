#!/usr/bin/env bash
if [[ "$@" =~ "." ]]
then 
  bc -l <<< "scale=3; $@"
else
  bc <<< "$@"
fi
