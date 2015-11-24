#!/bin/sh
mkdir -p "build" && \
echo "Building services..." && \
javac -d "build" -classpath "build" $(echo `pwd`)/src/org/cackharot/services/HelloService.java && \
javac -d "build" -classpath "build" $(echo `pwd`)/src/org/cackharot/services/publisher/HelloServicePublisher.java && \
java  -classpath "build" org.cackharot.services.publisher.HelloServicePublisher
