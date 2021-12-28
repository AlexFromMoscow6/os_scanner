#!/usr/bin/bash

yum=$(which yum)
apt=$(which apt)

if [[ ! -z $yum ]]; then
    sudo yum update -y && sudo yum -y install scrot python3-tk python3-dev
 elif [[ ! -z $apt ]]; then
    sudo apt update && sudo apt -y install scrot python3-tk python3-dev
fi

