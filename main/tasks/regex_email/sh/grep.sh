#/usr/bin/env sh

cat "$1" | grep -swo "[[:alnum:]]\+@[[:alnum:]]\+\.[[:alnum:]]\+" | sort | uniq
