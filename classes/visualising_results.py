import collections
import numpy as np
from matplotlib import pyplot as plt
from classes.statistical_analysis_class import StatisticalAnalysis
from functions.functions_ import generate_index_dict


class Visualizing_Results(StatisticalAnalysis):

    def show_data(self):
        plt.scatter(self.column('extreme_score'), self.column('PPCS_score'))
        plt.show()

    def bar_graph(self, column_string, data_not_a_string=False):
        if data_not_a_string:
            column = column_string
        else:
            column = self.column(column_string)
        column_dict = generate_index_dict(column)

        value = list(column_dict.keys())
        people = list(column_dict.values())

        plt.bar(value, people, color='maroon',
                width=0.4)

        plt.xlabel("Values")
        plt.ylabel("People")

        plt.show()

    def sex_double_graph_bar_scale(self, column_string, degrees=10):
        male_data, female_data = self.split_column_into_sexes(column_string)
        male_dict = generate_index_dict(male_data)
        female_dict = generate_index_dict(female_data)

        print(f'Males = {len(male_data)}')
        print(f'Females = {len(female_data)}')
        print(f'n = {len(male_data) + len(female_data)}')

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

    def sex_double_graph_bar_time(self, column_string):
        male_data, female_data = self.split_column_into_sexes(column_string)
        male_dict = generate_index_dict(male_data)
        female_dict = generate_index_dict(female_data)

        print(f'Males = {len(male_data)}')
        print(f'Females = {len(female_data)}')
        print(f'n = {len(male_data) + len(female_data)}')

        ordered_male_dict = split_into_groups(male_dict)
        ordered_female_dict = split_into_groups(female_dict)

        labels = ordered_male_dict.keys()

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
        ax.set_xlabel('Minutes')
        ax.set_title(f'Self evaluated {column_string}')
        ax.set_xticks(x, labels)
        ax.legend()

        ax.bar_label(bar_1, padding=3)
        ax.bar_label(bar_2, padding=3)

        fig.tight_layout()

        plt.show()

    def sex_double_graph_bar_extreme_score(self, column_string):
        male_data, female_data = self.split_column_into_sexes(column_string)
        male_dict = generate_index_dict(male_data)
        female_dict = generate_index_dict(female_data)

        print(f'Males = {len(male_data)}')
        print(f'Females = {len(female_data)}')
        print(f'n = {len(male_data) + len(female_data)}')

        ordered_male_dict = split_into_groups_extreme(male_dict)
        ordered_female_dict = split_into_groups_extreme(female_dict)

        labels = ordered_male_dict.keys()

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
        ax.set_xlabel('Scores')
        ax.set_title(f'Self evaluated {column_string}')
        ax.set_xticks(x, labels)
        ax.legend()

        ax.bar_label(bar_1, padding=3)
        ax.bar_label(bar_2, padding=3)

        fig.tight_layout()

        plt.show()

    def scatter_plot(self, column_string_1, column_string_2):
        y = self.column(column_string_1)
        x = self.column(column_string_2)

        plt.plot(x, y, 'o')

        plt.ylabel(column_string_1)
        plt.xlabel(column_string_2)
        m, b = np.polyfit(x, y, 1)

        plt.plot(x, m * np.array(x) + b)
        plt.show()


def split_into_groups(data_dict):
    sorted_dictionary = {'1-10': 0,
                         '10-20': 0,
                         '20-30': 0,
                         '30-60': 0,
                         '60-90': 0,
                         '90-120': 0,
                         '120-150': 0,
                         '150-240': 0,
                         '240-360': 0,
                         '360+': 0}

    for key, value in data_dict.items():
        key = round(key)
        if key in range(0, 11):
            sorted_dictionary['1-10'] += value
        elif key in range(11, 21):
            sorted_dictionary['10-20'] += value
        elif key in range(21, 31):
            sorted_dictionary['20-30'] += value
        elif key in range(31, 61):
            sorted_dictionary['30-60'] += value
        elif key in range(61, 91):
            sorted_dictionary['60-90'] += value
        elif key in range(91, 121):
            sorted_dictionary['90-120'] += value
        elif key in range(121, 151):
            sorted_dictionary['120-150'] += value
        elif key in range(151, 241):
            sorted_dictionary['150-240'] += value
        elif key in range(241, 361):
            sorted_dictionary['240-360'] += value
        elif key in range(361, 3000):
            sorted_dictionary['360+'] += value
        else:
            print(f' Error with {key}, {value}')

    return sorted_dictionary


def split_into_groups_extreme(data_dict):
    sorted_dictionary = {'1-2': 0,
                         '2-3': 0,
                         '3-4': 0,
                         '4-5': 0,
                         '5-6': 0
                         }

    for key, value in data_dict.items():
        if key < 2:
            sorted_dictionary['1-2'] += value
        elif key < 3:
            sorted_dictionary['2-3'] += value
        elif key < 4:
            sorted_dictionary['3-4'] += value
        elif key < 5:
            sorted_dictionary['4-5'] += value
        elif key > 5:
            sorted_dictionary['5-6'] += value
        else:
            print(f' Error with {key}, {value}')

    return sorted_dictionary
