#!/bin/bash
cd /home/ubuntu/Devops-Automation-Scripts || exit
#git pull origin master
git fetch --all
git reset --hard origin/master

