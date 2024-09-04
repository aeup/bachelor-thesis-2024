import csv

import matplotlib.pyplot as plt

file_name_mapping_array = [
    ("breadth-first", "Breadth-First"),
    ("depth-first", "Depth-First"),
    ("min-intermediate", "Min Intermediate")
]

testcases = [
    #("autoencoder","Autoencoder"),
    #("decisionTree","decisionTree"),
    #("kmeans", "kMeans"),
    #("lmCG", "lmCG"),
    #("multiLogReg", "multiLogReg"),
    #("pca", "PCA"),
    #("pnmf", "PNMF"),
    ("slicefinder_Adult", "slicefinder Adult Dataset"),
    ("slicefinder_Covtype", "slicefinder Covtype Dataset"),
    ("slicefinder_USCensus", "slicefinder US Census Dataset"),
    #("stratstats", "stratstats")
]


for (file_name, display_name) in file_name_mapping_array:
    for (testcase_file, (testcase_name)) in testcases:
        with open('temp/MEMORY_'+file_name+'_'+testcase_file+'.csv', newline='') as f:
            file_array = []
            time_array = []
            memory_array = []

            reader = csv.reader(f, delimiter=";")
            for row in reader:
                file_array.append(row)

            for i in range(int(len(file_array) / 2)):
                for j in range(len(file_array[i*2])):
                    if not(j == 0 or j == 1 or j == (len(file_array[i*2]) - 1)):
                        time_array.append(int(file_array[i*2][j]))
                        memory_array.append(int(file_array[i*2+1][j]))

            fig, ax = plt.subplots()
            ax.scatter(time_array, memory_array)#, c='b')
            # ax.scatter(time_array[1::2], memory_array[1::2], c='r')
            ax.set_xlabel("Time in ms")
            ax.set_ylabel("Memory Consumption in MB")
            plt.savefig('results/MEMORY_OVER_TIME_'+file_name+'_'+testcase_file+'.png')
