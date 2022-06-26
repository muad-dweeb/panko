#!/bin/bash

cd ${HOME}/panko
nohup ${HOME}/.virtualenvs/panko/bin/python3 ${HOME}/panko/app.py >> /var/log/panko.log 2>&1 &
