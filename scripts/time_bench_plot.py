import csv
import matplotlib.pyplot as plt

file_name_mapping_array = [
    ("breadth-first", "Breadth-First"),
    ("depth-first", "Depth-First"),
    ("min-intermediate", "Min Intermediate"),
    ("resource-aware", "Fast Resource-aware")
]

testcases = [
    #("autoencoder","Autoencoder"),
    ("decisionTree","decisionTree"),
    ("kmeans", "kMeans"),
    ("lmCG", "lmCG"),
    ("multiLogReg", "multiLogReg"),
    ("pca", "PCA"),
    ("pnmf", "PNMF"),
    #("slicefinder", "slicefinder"),
    ("stratstats", "stratstats")
]

datasets = [
    ("Adult", "Adult Dataset"),
    ("Covtype", "Covertype Dataset"),
    ("USCensus", "USCensus Dataset")
]

times = [
    ("TOTAL_COMPILATION_TIME", "compilation time"),
    ("TOTAL_ELAPSED_TIME", "total elapsed time"),
    ("TOTAL_EXECUTION_TIME", "execution time"),
]

for (time_file, time_name) in times:
    for (testcase_file, testcase_name) in testcases:

        results = []
        
        for (dataset_name, dataset_display_name) in datasets:

            results_dataset = []

            for (file_name, display_name) in file_name_mapping_array:
                file_array = []

                with open('temp/' + time_file + '_' + file_name + '_' + testcase_file + '_' + dataset_name + '.csv', newline='') as f:
                    reader = csv.reader(f, delimiter=";")

                    for row in reader:
                        file_array.append(row)

                measured_values = []
                for row in file_array:
                    for element in row:
                        measured_values.append(float(element.replace(",", ".")))

                results_dataset.append(measured_values)
            
            results.append(results_dataset)
            

        # generate plots
        fig, (chart1, chart2, chart3) = plt.subplots(1, 3)


        highest_over_all_value = max(max(x) for x in results[0])

        chart1.boxplot(results[0], labels=[i[0] for i in file_name_mapping_array], medianprops=dict(color="black"))
        chart1.set_ylim(0, highest_over_all_value + 0.1 * highest_over_all_value)
        plt.setp(chart1.get_xticklabels(), rotation=60, horizontalalignment='right')
        chart1.set_ylabel("runtime in s")


        highest_over_all_value = max(max(x) for x in results[1])

        chart2.boxplot(results[1], labels=[i[0] for i in file_name_mapping_array], medianprops=dict(color="black"))
        chart2.set_ylim(0, highest_over_all_value + 0.1 * highest_over_all_value)
        plt.setp(chart2.get_xticklabels(), rotation=60, horizontalalignment='right')
        chart2.set_ylabel("runtime in s")

        highest_over_all_value = max(max(x) for x in results[2])

        chart3.boxplot(results[2], labels=[i[0] for i in file_name_mapping_array], medianprops=dict(color="black"))
        chart3.set_ylim(0, highest_over_all_value + 0.1 * highest_over_all_value)
        plt.setp(chart3.get_xticklabels(), rotation=60, horizontalalignment='right')
        chart3.set_ylabel("runtime in s")

        fig.tight_layout()

        plt.savefig('results/' + time_file +'_' + testcase_file + '.png')

        plt.close(fig)
