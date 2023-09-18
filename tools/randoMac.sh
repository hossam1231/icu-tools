#!/bin/bash

# v 1.0.2
# https://gist.github.com/mbierman/03b2a962ac04963ef5bbc8354d0ed5d1
# 2022 mbierman

sleep="${1:-5}"
regex="^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$"
getmac () {
	rnd=$(openssl rand -hex 6 | sed 's/\(..\)\(..\)\(..\)\(..\)\(..\)\(..\)/\1:\2:\3:\4:\5:\6/')
	echo -e  "What is the mac address want to set the mac\n\nexample: CA:49:63:9F:78:27\n\nLeave blank to get one generated for you."
	read tmp
	mac1=${tmp:=$rnd}

	mac=$(echo $mac1 | tr '[:lower:]' '[:upper:]')
	
	if [[ $mac =~ $regex ]] ; then
		comp=true
		echo -e "\n\n Using $mac...\n"
	else
		comp=false
		echo false	
	fi 
}

until [ "$comp" = "true" ]
do
	getmac
done

getAdapter () {
echo "What is the adapter you want to set the mac for [en0,en1, etc. use 'ifconfig' if you don't know]"
read adapter
}
until [ "$adapter" ] 
do
	getAdapter
done

type=$(ifconfig $adapter | grep baseT)
if [ "$type" ]; then
	echo "got Ethernet"
	type="Ethernet"
else
	echo "got Wi-Fi"
	type="Wi-Fi"
fi

read -p "Is $adapter $type (y|n) ? " -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]];  then
	echo "Exiting. Run again"
	exit
fi 

sudo ifconfig $adapter down && sleep $sleep  && sudo ifconfig $adapter up && \
sudo ifconfig $adapter ether $mac && sudo networksetup -detectnewhardware