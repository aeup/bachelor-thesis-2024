echo "Installing dependencies..."
#sudo apt update
#sudo apt install -y git openjdk-11-jdk maven r-base

#export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH

echo "Setting up SystemDS..."
rm -rf dependencies
mkdir -p dependencies
cd dependencies
git clone git@github.com:aeup/systemds.git

cd systemds
export SYSTEMDS_ROOT=$(pwd)
export PATH=$SYSTEMDS_ROOT/bin:$PATH

echo "Installing test dependencies..."
Rscript ./src/test/scripts/installDependencies.R

echo "Building SystemDS..."
mvn package -P distribution

echo "SystemDS is set up."