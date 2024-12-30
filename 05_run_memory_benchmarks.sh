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

    > temp/MEMORY_${CONFIG_NAME}_${DML_NAME}.csv

    echo -e "-----\nCONFIG: ${CONFIG_FILE}\nDML FILE: $DML_FILE\n"

    for (( i = 1; i <= $RUNS; i++ )); do

      #systemds -f $DML_FILE --config $CONFIG_FILE
      LOGS="$(systemds -f $DML_FILE --config $CONFIG_FILE -stats)"
      MEMORY_CONSUMPTION="$(echo "$LOGS" |grep "MemoryMonitor:")"

      REGEX1='[[:space:]][0-9]+[[:space:]]'
      REGEX2='[0-9]+'
      REGEX3='[[0-9]+]'

      TIME="$(echo ${MEMORY_CONSUMPTION} | grep -Eo $REGEX3 | grep -Eo $REGEX2 | paste -s -d ";")"
      MEMORY="$(echo ${MEMORY_CONSUMPTION} | grep -Eo $REGEX1 | grep -Eo $REGEX2 | paste -s -d ";")"

      if [ "$LOG_LEVEL" = "FULL" ]; then
        echo "$LOGS"
      fi

      echo "TIME;${TIME}" >> temp/MEMORY_${CONFIG_NAME}_${DML_NAME}.csv
      echo "MEMORY;START;${MEMORY};END" >> temp/MEMORY_${CONFIG_NAME}_${DML_NAME}.csv
    done

    echo "-----"
  done
done
