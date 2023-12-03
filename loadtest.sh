#! /usr/bin/bash

for i in $(seq 1 5000)
do
	curl http://localhost:8080
done

