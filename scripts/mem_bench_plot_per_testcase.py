import csv
import matplotlib.pyplot as plt
import numpy as np
import copy

file_name_mapping_array = [
    ("breadth-first", "Breadth-First"),
    ("depth-first", "Depth-First"),
    ("min-intermediate", "Min Intermediate"),
    ("resource-aware", "Fast Resource-aware")
]

datasets = [
    ("Adult", "Adult Dataset"),
    ("Covtype", "Covertype Dataset"),
    ("USCensus", "USCensus Dataset")
]

testcases = [
    ("decisionTree","decisionTree", datasets),
    ("kmeans", "kMeans", datasets),
    ("lmCG", "lmCG", datasets),
    ("multiLogReg", "multiLogReg", datasets),
    ("pca", "PCA", datasets),
    ("pnmf", "PNMF", datasets),
    ("slicefinder", "slicefinder", datasets[:2]), # only generate for Adult and Covtype datasets
    ("stratstats", "stratstats", datasets[:1]) # only generate for Adult dataset
]

keywords = [
    "MEMORY",
    "START",
    "END"
]

for (testcase_file, testcase_name, testcase_datasets) in testcases:

    results = []

    for dataset_id, (dataset, dataset_description) in enumerate(testcase_datasets):

        dataset_results = []

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

                    dataset_results.append(highest_measured_value)

            except:
                print('FILE temp/MEMORY_' + file_name + '_' + testcase_file + '_' + dataset + '.csv NOT FOUND')
        
        results.append(dataset_results)

    # generate plots
    hatch = ['/', '+', 'X' , '-']

    if(len(testcase_datasets) == 3):
        fig, (chart1, chart2, chart3) = plt.subplots(1, 3)

        highest_over_all_value = max(results[0])

        chart1.bar([0, 1, 2, 3], results[0], 0.8, hatch=hatch, label=[i[1] for i in file_name_mapping_array], edgecolor='black', color='lightgrey')
        chart1.set_ylim(0, highest_over_all_value + 0.2 * highest_over_all_value)
        chart1.set_ylabel("Memory Consumption in MB")
        chart1.tick_params(axis='x', which='both', bottom=False,top=False, labelbottom=False)
        chart1.set_title(datasets[0][1])

        highest_over_all_value = max(results[1])

        chart2.bar([0, 1, 2, 3], results[1], 0.8, hatch=hatch, label=[i[1] for i in file_name_mapping_array], edgecolor='black', color='lightgrey')
        chart2.set_ylim(0, highest_over_all_value + 0.2 * highest_over_all_value)
        chart2.set_ylabel("Memory Consumption in MB")
        chart2.tick_params(axis='x', which='both', bottom=False,top=False, labelbottom=False)
        chart2.set_title(datasets[1][1])

        highest_over_all_value = max(results[2])

        chart3.bar([0, 1, 2, 3], results[2], 0.8, hatch=hatch, label=[i[1] for i in file_name_mapping_array], edgecolor='black', color='lightgrey')
        chart3.set_ylim(0, highest_over_all_value + 0.2 * highest_over_all_value)
        chart3.set_ylabel("Memory Consumption in MB")
        chart3.tick_params(axis='x', which='both', bottom=False,top=False, labelbottom=False)
        chart3.set_title(datasets[2][1])
    
    if(len(testcase_datasets) == 2):
        fig, (chart1, chart2) = plt.subplots(1, 2)

        highest_over_all_value = max(results[0])

        chart1.bar([0, 1, 2, 3], results[0], 0.8, hatch=hatch, label=[i[1] for i in file_name_mapping_array], edgecolor='black', color='lightgrey')
        chart1.set_ylim(0, highest_over_all_value + 0.2 * highest_over_all_value)
        chart1.set_ylabel("Memory Consumption in MB")
        chart1.tick_params(axis='x', which='both', bottom=False,top=False, labelbottom=False)
        chart1.set_title(datasets[0][1])

        highest_over_all_value = max(results[1])

        chart2.bar([0, 1, 2, 3], results[1], 0.8, hatch=hatch, label=[i[1] for i in file_name_mapping_array], edgecolor='black', color='lightgrey')
        chart2.set_ylim(0, highest_over_all_value + 0.2 * highest_over_all_value)
        chart2.set_ylabel("Memory Consumption in MB")
        chart2.tick_params(axis='x', which='both', bottom=False,top=False, labelbottom=False)
        chart2.set_title(datasets[1][1])
    
    if(len(testcase_datasets) == 1):
        fig, chart1 = plt.subplots(1, 1)

        highest_over_all_value = max(results[0])

        chart1.bar([0, 1, 2, 3], results[0], 0.8, hatch=hatch, label=[i[1] for i in file_name_mapping_array], edgecolor='black', color='lightgrey')
        chart1.set_ylim(0, highest_over_all_value + 0.2 * highest_over_all_value)
        chart1.set_ylabel("Memory Consumption in MB")
        chart1.tick_params(axis='x', which='both', bottom=False,top=False, labelbottom=False)
        chart1.set_title(datasets[0][1])

    fig.tight_layout()
    handles, labels = chart1.get_legend_handles_labels()
    legend = fig.legend(handles, labels, loc='upper center', ncol=2, bbox_to_anchor=(0.5,0))
    plt.savefig('results/MEMORY_' + testcase_file + '.png', dpi=400,  bbox_extra_artists=(legend,), bbox_inches='tight')

    plt.close(fig)
