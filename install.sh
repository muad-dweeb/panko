#!/bin/bash

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

logfile=/var/log/panko.log
user=$(whoami)

sudo touch $logfile
sudo chown $user $logfile

python3 -m venv ${HOME}/.virtualenvs/panko


symlink=${HOME}/panko
if [ ! -e $symlink ]; then
  ln -s $SCRIPT_DIR $symlink
fi

