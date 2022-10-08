from matplotlib import pyplot as plt

from classes.statistical_analysis_class import StatisticalAnalysis


def generate_index_dict(column):
    column_dict = {}

    for item in column:
        if item in column_dict:
            column_dict[item] += 1
        else:
            column_dict[item] = 1

    return column_dict


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
