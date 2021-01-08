#!/bin/sh
mkdir -p "build" && \
echo "Building services..." && \
javac -d "build" -cp "$(pwd)/jaxws-ri/lib/*" "$(pwd)/src/org/InfoService.java" && \
javac -d "build" -cp "$(pwd)/jaxws-ri/lib/*" "$(pwd)/src/org/HelloService.java" && \
javac -d "build" -cp "build:$(pwd)/jaxws-ri/lib/*" "$(pwd)/src/org/HelloServicePublisher.java" && \
java -cp "build:$(pwd)/jaxws-ri/lib/*" org.HelloServicePublisher
