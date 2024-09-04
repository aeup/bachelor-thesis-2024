import csv
import matplotlib.pyplot as plt
import numpy as np
import copy

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
    ("slicefinder", "slicefinder"),
    #("stratstats", "stratstats")
]

datasets = [
    ("Adult", "Adult Dataset"),
    ("Covtype", "Covtype Dataset"),
    ("USCensus", "USCensus Dataset")
]

keywords = [
    "MEMORY",
    "START",
    "END"
]

for (testcase_file, testcase_name) in testcases:

    # generate results dictonary
    results = {}
    for (file_name, display_name) in file_name_mapping_array:
        results[file_name] = [None] * len(datasets)

    # needed fpr plotting
    highest_over_all_value = 0

    for dataset_id, (dataset, dataset_description) in enumerate(datasets):

        for file_id, (file_name, display_name) in enumerate(file_name_mapping_array):
            try:
                with open('temp/MEMORY_' + file_name + '_' + testcase_file + '_' + dataset + '.csv', newline='') as f:

                    file_array = []
                    highest_measured_value = 0

                    reader = csv.reader(f, delimiter=";")

                    for row in reader:
                        file_array.append(row)

                    memory_array = file_array[1::2]

                    for run_array in memory_array:
                        for measured_value in run_array:
                            if not (measured_value in keywords):

                                value_as_int = int(measured_value)

                                if value_as_int > highest_measured_value:
                                    highest_measured_value = value_as_int

                    results[file_name][dataset_id] = highest_measured_value

                    if highest_over_all_value < highest_measured_value:
                        highest_over_all_value = highest_measured_value
            except:
                print('FILE temp/MEMORY_' + file_name + '_' + testcase_file + '_' + dataset + '.csv NOT FOUND')

    temp_dataset = list(datasets)
    temp_results = copy.deepcopy(results)
    removed_datasets = 0

    for i, result in enumerate(results[file_name_mapping_array[0][0]]):
        if result == None:
            temp_dataset.pop(i - removed_datasets)
            for j, temp in enumerate(temp_results):
                temp_results[file_name_mapping_array[j][0]].pop(i - removed_datasets)
            removed_datasets += 1

    if len(temp_dataset) == 0:
        print('Cannot create Plot for Testcase: ' + testcase_name)
        break

    # generate plots

    label_location = np.arange(len(temp_dataset))
    bar_width = 0.3
    multiplier = 0


    fig, chart = plt.subplots(layout='constrained')

    for file_id, (file_name, result) in enumerate(temp_results.items()):
        offset = bar_width * multiplier
        rects = chart.bar( label_location + offset, result, bar_width, label=file_name_mapping_array[file_id][0])
        chart.bar_label(rects, padding=3)
        multiplier += 1




    chart.set_title(testcase_name)
    chart.set_ylabel("Memory Consumption in MB")
    chart.set_xticks(label_location + bar_width, [i[1] for i in temp_dataset])
    chart.legend(loc='upper left', ncols=3)
    chart.set_ylim(0, highest_over_all_value + 2000)

    plt.savefig('results/MEMORY_' + testcase_file + '.png')
