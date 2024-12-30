## Reproducibility: Resource-aware Operator Scheduling in ML Systems

**Source Code Info:**
* Repository: <https://github.com/aeup/systemds> (commit 799ab3e6da8a718349fe874230e8e4d6209b60aa)
* Reproducibility Repository: <https://github.com/aeup/bachelor-thesis-2024>

**Required Dependencies**
* java, maven, r-base
* git
* python3, matplotlib


**Used Datasets:**
* Adult: <https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data>
* Covertype: <https://archive.ics.uci.edu/ml/machine-learning-databases/covtype/covtype.data.gz>
* USCensus: <https://archive.ics.uci.edu/static/public/116/us+census+data+1990.zip>

**Experimental Setup**
The experiments in the thesis were executed on the following system:
* Processor: AMD EPYC 7443P 24-Core Processor (24 cores, 48 threads, 2.85 GHz)
* Memory: 256 GB DDR4 at 3.2 GHz
* Storage: 480 GiB SATA SSD
* OS: Ubuntu 20.04.6 LTS
* Java Version: 11 with
* Apache SystemDS parameter: -Xmx250g -Xms250g

**Setup and Experiments:**
    
    ./01_setup_systemds.sh

    # change the Apache SystemDS parameter in this step

    ./02_download_data.sh
    ./03_run_time_benchmarks.sh
    ./04_reconfigure_systemds.sh
    ./05_run_memory_benchmarks.sh
    ./06_run_python_scripts.sh

The generated figures are saved in *results*. The results used in the thesis are saved in *data_used_in_thesis*.