#!/bin/bash

logfile=/var/log/panko.log
user=$(whoami)

sudo touch $logfile
sudo chown $user $logfile

