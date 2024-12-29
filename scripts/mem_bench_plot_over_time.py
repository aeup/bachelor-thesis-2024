import csv

import matplotlib.pyplot as plt

testcases = [
    ('MEMORY_resource-aware_multiLogReg_Adult.csv', 'MEMORY_OVER_TIME_multiLogReg_Adult.png'),
    ('MEMORY_resource-aware_stratstats_Adult.csv', 'MEMORY_OVER_TIME_stratstats.png')
]

for (file_name, output_file_name) in testcases:
    with open('temp/'+file_name, newline='') as f:
        file_array = []
        time_array = []
        memory_array = []

        reader = csv.reader(f, delimiter=";")
        for row in reader:
            file_array.append(row)

        for j in range(len(file_array[0])):
            # removes the data pairs that are markers and no real data
            if not(j == 0 or j == 1 or j == (len(file_array[0]) - 1)):
                time_array.append(int(file_array[0][j]) / 1000)
                memory_array.append(int(file_array[1][j]))

        fig, ax = plt.subplots()
        ax.plot(time_array, memory_array, color="black")
        ax.set_ylim(ymin=0)
        ax.set_xlim(xmin=0)
        ax.set_xlabel("Time in s")
        ax.set_ylabel("Memory Consumption in MB")
        plt.savefig('results/'+output_file_name)
