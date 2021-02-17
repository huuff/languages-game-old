#/usr/bin/env sh

addresses=`cat "$2" | grep -swo "[[:alnum:]]\+@[[:alnum:]]\+\.[[:alnum:]]\+" | sort | uniq`
#if [[ "$1" == "address" ]]
#then
  #echo "$addresses"
#fi

case "$1" in
  "address")
    echo "$addresses"
    ;;
  "domains")
    echo "$addresses" | cut -f2 -d@ | sort | uniq
    ;;
  "tlds")
    echo "$addresses" | cut -f2 -d. | sort | uniq
esac
