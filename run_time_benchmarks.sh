DML_FILES=(testcases/*.dml)
CONFIG_FILES=(configs/*.xml)
RUNS=5

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

    > temp/TIME_${CONFIG_NAME}_${DML_NAME}.csv

    echo -e "-----\nCONFIG: ${CONFIG_FILE}\nDML FILE: $DML_FILE\n"

    for (( i = 1; i <= $RUNS; i++ )); do

      LOGS="$(systemds -f $DML_FILE -config $CONFIG_FILE)"
      TOTAL_EXECUTION_TIME="$(echo "$LOGS" | grep "Total execution time:")"

      REGEX='[0-9]+,[0-9]+'
      TIME="$(echo ${TOTAL_EXECUTION_TIME} | grep -Eo $REGEX)"

      if [ "$LOG_LEVEL" = "FULL" ]; then
      echo "$LOGS"
      fi

      echo -n "${TIME}" >> temp/TIME_${CONFIG_NAME}_${DML_NAME}.csv

      if [ $i -lt $RUNS ]; then
        echo -n ";" >> temp/TIME_${CONFIG_NAME}_${DML_NAME}.csv
      fi
    done

    echo "-----"
  done
done

python3 scripts/time_bench_plot.py
