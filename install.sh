#!/bin/bash

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

logfile=/var/log/panko.log
user=$(whoami)

sudo touch $logfile
sudo chown $user $logfile

venv_path=${HOME}/.virtualenvs/panko
python3 -m venv $venv_path
source ${venv_path}/bin/activate
pip3 install -r requirements.txt

symlink=${HOME}/panko
if [ ! -e $symlink ]; then
  ln -s $SCRIPT_DIR $symlink
fi

