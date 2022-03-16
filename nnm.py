#!/usr/bin/env python
import os
import subprocess
#Changing Python working directory to script directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#Get activation code from user and prepend activation CLI
activation_code = input('Please press enter and input your activation code. If connecting to Labbox, enter SecurityCenter.')
with open("activationcode.txt", "w") as f:
  f.write(input())
with open('activationcode.txt', 'r') as f:
    lines = f.readlines()
lines = ['eval /opt/nnm/bin/nnm -a '+line for line in lines]
with open('activationcode.txt', 'w') as f:
    f.writelines(lines)
verify_network = subprocess.run([
    "docker", "network", "create", "docker_labbox_default"])
#Lets build a Docker image :D
build_docker = subprocess.run([
    "docker", "build", "./", "-f", "Dockerfile", "-t", "nnm-image"])
#Bring dat container up
docker_compose = subprocess.run([
    "docker-compose", "up", "-d"])
#Activate NNM like a boss
build_docker = subprocess.run([
    "docker", "exec", "nnm-labbox", "bash", "-c", "./usr/bin/activationcode.txt"])
#Force NNM to start
start_nnm = subprocess.run([
    "docker", "exec", "-d", "nnm-labbox", "/opt/nnm/bin/nnm"])
#Set Monitored Range
nnm_range = subprocess.run([
    "docker", "exec", "nnm-labbox", "/opt/nnm/bin/nnm", "--config", "Monitored Network IP Addresses and Ranges", "0.0.0.0/8"])
#Remove Complex Passwords
nnm_pw = subprocess.run([
    "docker", "exec", "nnm-labbox", "/opt/nnm/bin/nnm", "--config", "Enforce Complex Passwords", "0"])
#Monitor Mode all the way
nnm_monitor = subprocess.run([
    "docker", "exec", "nnm-labbox", "/opt/nnm/bin/nnm", "--config", "Run in Discovery Mode", "0"])
#Change password
change_pw = subprocess.run([
    "docker", "exec", "nnm-labbox", "/opt/nnm/bin/nnm", "--users", "--chpasswd", "admin", "password"])
