#!/bin/bash
PW=$1
docker login -u simongineiger --password-stdin $PW
dockerpath=simongineiger/udacity_devops_capstone
docker tag xclapi $dockerpath
docker push $dockerpath





