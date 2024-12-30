import csv
import matplotlib.pyplot as plt

params = {'legend.fontsize': 'large',
         'axes.labelsize': 'large',
         'xtick.labelsize':'large',
         'ytick.labelsize':'large'}
plt.rcParams.update(params)

file_name_mapping_array = [
    ("breadth-first", "(b)"),
    ("depth-first", "(d)"),
    ("min-intermediate", "(m)"),
    ("resource-aware", "(r)")
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

for (time_file, time_name) in times:
    for (testcase_file, testcase_name, testcase_datasets) in testcases:

        results = []
        
        for (dataset_name, dataset_display_name) in testcase_datasets:

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
        if(len(testcase_datasets) == 3):
            fig, (chart1, chart2, chart3) = plt.subplots(1, 3)

            highest_over_all_value = max(max(x) for x in results[0])

            chart1.boxplot(results[0], labels=[i[1] for i in file_name_mapping_array], medianprops=dict(color="black"))
            chart1.set_ylim(0, highest_over_all_value + 0.1 * highest_over_all_value)
            chart1.set_ylabel("Time in s")
            chart1.set_title(datasets[0][1])

            highest_over_all_value = max(max(x) for x in results[1])

            chart2.boxplot(results[1], labels=[i[1] for i in file_name_mapping_array], medianprops=dict(color="black"))
            chart2.set_ylim(0, highest_over_all_value + 0.1 * highest_over_all_value)
            chart2.set_ylabel("Time in s")
            chart2.set_title(datasets[1][1])

            highest_over_all_value = max(max(x) for x in results[2])

            chart3.boxplot(results[2], labels=[i[1] for i in file_name_mapping_array], medianprops=dict(color="black"))
            chart3.set_ylim(0, highest_over_all_value + 0.1 * highest_over_all_value)
            chart3.set_ylabel("Time in s")
            chart3.set_title(datasets[2][1])
        
        if(len(testcase_datasets) == 2):
            fig, (chart1, chart2) = plt.subplots(1, 2)

            highest_over_all_value = max(max(x) for x in results[0])

            chart1.boxplot(results[0], labels=[i[1] for i in file_name_mapping_array], medianprops=dict(color="black"))
            chart1.set_ylim(0, highest_over_all_value + 0.1 * highest_over_all_value)
            chart1.set_ylabel("Time in s")
            chart1.set_title(datasets[0][1])


            highest_over_all_value = max(max(x) for x in results[1])

            chart2.boxplot(results[1], labels=[i[1] for i in file_name_mapping_array], medianprops=dict(color="black"))
            chart2.set_ylim(0, highest_over_all_value + 0.1 * highest_over_all_value)
            chart2.set_ylabel("Time in s")
            chart2.set_title(datasets[1][1])
        
        if(len(testcase_datasets) == 1):
            fig, (chart1) = plt.subplots(1, 1)

            highest_over_all_value = max(max(x) for x in results[0])

            chart1.boxplot(results[0], labels=[i[1] for i in file_name_mapping_array], medianprops=dict(color="black"))
            chart1.set_ylim(0, highest_over_all_value + 0.1 * highest_over_all_value)
            chart1.set_ylabel("Time in s")
            chart1.set_title(datasets[0][1])


        fig.tight_layout()

        plt.savefig('results/' + time_file +'_' + testcase_file + '.png', dpi=400)

        plt.close(fig)
