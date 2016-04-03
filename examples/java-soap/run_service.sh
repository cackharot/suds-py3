#!/bin/sh
mkdir -p "build" && \
echo "Building services..." && \
javac -d "build" -classpath "build" $(echo `pwd`)/src/org/InfoService.java && \
javac -d "build" -classpath "build" $(echo `pwd`)/src/org/HelloService.java && \
javac -d "build" -classpath "build" $(echo `pwd`)/src/org/HelloServicePublisher.java && \
java  -classpath "build" org.HelloServicePublisher
