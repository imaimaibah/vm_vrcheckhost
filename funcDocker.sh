#!/bin/bash

function testrun(){
	docker run -w /var/tmp/vm_vrcheckhost --volume /home/shin/Scripts/:/var/tmp --rm python python vm_vrAlert.py
}
