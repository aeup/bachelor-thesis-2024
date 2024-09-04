import csv
import matplotlib.pyplot as plt

file_name_mapping_array = [
    ("breadth-first", "Breadth-First"),
    ("depth-first", "Depth-First"),
    ("min-intermediate", "Min Intermediate")
]

testcases = [
    ("autoencoder","Autoencoder"),
    ("decisionTree","decisionTree"),
    ("kmeans", "kMeans"),
    ("lmCG", "lmCG"),
    ("multiLogReg", "multiLogReg"),
    ("pca", "PCA"),
    ("pnmf", "PNMF"),
    ("slicefinder", "slicefinder"),
    ("stratstats", "stratstats")
]

for (testcase_file, testcase_name) in testcases:
    results = []

    for (file_name, display_name) in file_name_mapping_array:
        file_array = []

        with open('temp/TIME_' + file_name + '_' + testcase_file + '.csv', newline='') as f:
            reader = csv.reader(f, delimiter=";")

            for row in reader:
                file_array.append(row)

        measured_values = []
        for row in file_array:
            for element in row:
                measured_values.append(float(element.replace(",", ".")))

        results.append(measured_values)

    # generate plots
    fig, chart = plt.subplots(1, 1)

    chart.boxplot(results, tick_labels=[i[0] for i in file_name_mapping_array])
    chart.set_title(testcase_name)
    chart.set_ylim(ymin=0)
    plt.setp(chart.get_xticklabels(), rotation=60, horizontalalignment='right')
    chart.set_ylabel("runtime in s")

    fig.tight_layout()

    plt.savefig('results/TIME_' + testcase_file + '.png')
