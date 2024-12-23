#!/bin/bash

export SYSTEMDS_ROOT=$(pwd)/dependencies/systemds/
export PATH=$SYSTEMDS_ROOT/bin:$PATH

DML_FILES=(testcases/*.dml)
CONFIG_FILES=(configs/*.xml)
RUNS=10

while getopts l: flag
do
    case "${flag}" in
        l) LOG_LEVEL=${OPTARG};;
        *) ;;
    esac
done

mkdir -p temp

for CONFIG_FILE in "${CONFIG_FILES[@]}"; do
  for DML_FILE in "${DML_FILES[@]}"; do

    REGEX_DML_NAME='(?<=\/).+?(?=\.dml)'
    DML_NAME=$(echo "${DML_FILE}" | grep -Po $REGEX_DML_NAME)

    REGEX_CONFIG_NAME='(?<=\/SystemDS-config-).+?(?=\.xml)'
    CONFIG_NAME=$(echo "${CONFIG_FILE}" | grep -Po $REGEX_CONFIG_NAME)

    > temp/TOTAL_ELAPSED_TIME_${CONFIG_NAME}_${DML_NAME}.csv
    > temp/TOTAL_COMPILATION_TIME_${CONFIG_NAME}_${DML_NAME}.csv
    > temp/TOTAL_EXECUTION_TIME_${CONFIG_NAME}_${DML_NAME}.csv

    echo -e "-----\nCONFIG: ${CONFIG_FILE}\nDML FILE: $DML_FILE\n"

    for (( i = 1; i <= $RUNS; i++ )); do

      echo -e "RUN: ${i}"

      LOGS="$(systemds -f $DML_FILE -config $CONFIG_FILE -stats)"
      TOTAL_ELAPSED_TIME="$(echo "$LOGS" | grep "Total elapsed time:")"
      TOTAL_COMPILATION_TIME="$(echo "$LOGS" | grep "Total compilation time:")"
      TOTAL_EXECUTION_TIME="$(echo "$LOGS" | grep "Total execution time:")"

      REGEX='[0-9]+,[0-9]+'
      TOTAL_ELAPSED_TIME="$(echo ${TOTAL_ELAPSED_TIME} | grep -Eo $REGEX)"
      TOTAL_COMPILATION_TIME="$(echo ${TOTAL_COMPILATION_TIME} | grep -Eo $REGEX)"
      TOTAL_EXECUTION_TIME="$(echo ${TOTAL_EXECUTION_TIME} | grep -Eo $REGEX)"

      if [ "$LOG_LEVEL" = "FULL" ]; then
      echo "$LOGS"
      fi

      echo -n "${TOTAL_ELAPSED_TIME}" >> temp/TOTAL_ELAPSED_TIME_${CONFIG_NAME}_${DML_NAME}.csv
      echo -n "${TOTAL_COMPILATION_TIME}" >> temp/TOTAL_COMPILATION_TIME_${CONFIG_NAME}_${DML_NAME}.csv
      echo -n "${TOTAL_EXECUTION_TIME}" >> temp/TOTAL_EXECUTION_TIME_${CONFIG_NAME}_${DML_NAME}.csv

      if [ $i -lt $RUNS ]; then
        echo -n ";" >> temp/TOTAL_ELAPSED_TIME_${CONFIG_NAME}_${DML_NAME}.csv
        echo -n ";" >> temp/TOTAL_COMPILATION_TIME_${CONFIG_NAME}_${DML_NAME}.csv
        echo -n ";" >> temp/TOTAL_EXECUTION_TIME_${CONFIG_NAME}_${DML_NAME}.csv
      fi
    done

    echo "-----"
  done
done

python3 scripts/time_bench_plot.py
