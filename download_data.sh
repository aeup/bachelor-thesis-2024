# this file is based on https://github.com/damslab/reproducibility/blob/master/sigmod2021-sliceline-p218/run3DownloadData.sh

mkdir -p data

# Adult
mkdir -p data/Adult
curl https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data -o ./data/Adult/Adult.csv;
sed -i '$d' data/Adult/Adult.csv;

systemds -f dataprep/dataprepAdult.dml -exec singlenode -stats -nvargs FILE="./data/Adult/Adult.csv" OUTPUTDIR="./data/Adult/"

# Adult Short
mkdir -p data/Adult/short

systemds -f dataprep/shortAdult.dml -stats -nvargs DIR="./data/Adult/" LENGTH=10000

# Covtype
mkdir -p data/Covtype
curl https://archive.ics.uci.edu/ml/machine-learning-databases/covtype/covtype.data.gz -o ./data/Covtype/covtype.data.gz;
gzip -d ./data/Covtype/covtype.data.gz;
mv ./data/Covtype/covtype.data ./data/Covtype/Covtype.csv;

systemds -f dataprep/dataprepCovtype.dml -exec singlenode -stats -nvargs FILE="./data/Covtype/Covtype.csv" OUTPUTDIR="./data/Covtype/"

# Covtype Short
mkdir -p data/Covtype/short

systemds -f dataprep/shortCovtype.dml -nvargs DIR="./data/Covtype/" LENGTH=200

# US Census
mkdir -p data/USCensus
curl https://archive.ics.uci.edu/static/public/116/us+census+data+1990.zip -o ./data/USCensus/USCensus.zip
unzip ./data/USCensus/USCensus.zip USCensus1990.data.txt USCensus1990.attributes.txt -d ./data/USCensus/

mv ./data/USCensus/USCensus1990.data.txt ./data/USCensus/USCensus.csv
mv ./data/USCensus/USCensus1990.attributes.txt ./data/USCensus/USCensus.attributes.csv

systemds -f dataprep/dataprepUSCensus.dml -exec singlenode -stats -nvargs FILE="./data/USCensus/USCensus.csv" OUTPUTDIR="./data/USCensus/"

# USCensus Short
mkdir -p data/USCensus/short

systemds -f dataprep/shortUSCensus.dml -nvargs DIR="./data/USCensus/" LENGTH=5000