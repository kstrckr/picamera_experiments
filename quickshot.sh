#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

raspistill -n -rot 180 -v -ex night -mm matrix -drc med -q 80 -o ./$DATE.jpg
