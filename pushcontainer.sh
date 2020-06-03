#!/usr/bin/env bash
withCredentials:
docker login -u simongineiger -p $creds

dockerpath=simongineiger/udacity_devops_capstone
docker tag xclapi $dockerpath
docker push $dockerpath





