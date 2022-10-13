import collections
import numpy as np
from matplotlib import pyplot as plt
from classes.statistical_analysis_class import StatisticalAnalysis
from functions.functions_ import generate_index_dict


class Visualizing_Results(StatisticalAnalysis):

    def show_data(self):
        plt.scatter(self.column('extreme_score'), self.column('PPCS_score'))
        plt.show()

    def bar_graph(self, column_string):

        column = self.column(column_string)
        column_dict = generate_index_dict(column)

        value = list(column_dict.keys())
        people = list(column_dict.values())

        plt.bar(value, people, color='maroon',
                width=0.4)

        plt.xlabel("Values")
        plt.ylabel("People")

        plt.show()

    def sex_double_graph_bar(self, column_string, degrees=10):
        male_data, female_data = self.split_column_into_sexes(column_string)
        male_dict = generate_index_dict(male_data)
        female_dict = generate_index_dict(female_data)

        degrees += 1
        labels = np.arange(1, degrees)

        for number in labels:
            if number not in male_dict.keys():
                male_dict[number] = 0
            if number not in female_dict.keys():
                female_dict[number] = 0

        ordered_male_dict = collections.OrderedDict(sorted(male_dict.items()))
        ordered_female_dict = collections.OrderedDict(sorted(female_dict.items()))

        female_values = list(ordered_female_dict.values())
        male_values = list(ordered_male_dict.values())

        men_means = female_values
        women_means = male_values

        x = np.arange(len(labels))
        width = 0.35

        fig, ax = plt.subplots()
        bar_1 = ax.bar(x - width / 2, men_means, width, label='Women')
        bar_2 = ax.bar(x + width / 2, women_means, width, label='Men')

        ax.set_ylabel('Amount of people')
        ax.set_xlabel('Self evaluated score')
        ax.set_title(f'Self evaluated {column_string}')
        ax.set_xticks(x, labels)
        ax.legend()

        ax.bar_label(bar_1, padding=3)
        ax.bar_label(bar_2, padding=3)

        fig.tight_layout()

        plt.show()
