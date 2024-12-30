#!/bin/bash

echo "Setting up SystemDS..."
rm -rf dependencies
mkdir -p dependencies
cd dependencies
git clone git@github.com:aeup/systemds.git
git checkout 799ab3e6da8a718349fe874230e8e4d6209b60aa

cd systemds
export SYSTEMDS_ROOT=$(pwd)
export PATH=$SYSTEMDS_ROOT/bin:$PATH

echo "Installing test dependencies..."
Rscript ./src/test/scripts/installDependencies.R

echo "Building SystemDS..."
mvn package -P distribution

echo "SystemDS is set up."