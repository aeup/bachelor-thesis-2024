#!/bin/bash

export SYSTEMDS_ROOT=$(pwd)
export PATH=$SYSTEMDS_ROOT/bin:$PATH

echo "Check out SystemDS branch with memory monitor..."
cd dependencies/systemds
git checkout memory-monitor

echo "Building SystemDS..."
mvn package -P distribution

echo "SystemDS is set up."