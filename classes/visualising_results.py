from matplotlib import pyplot as plt

from classes.statistical_analysis_class import StatisticalAnalysis


class Visualizing_Results(StatisticalAnalysis):

    def show_data(self):
        plt.scatter(self.column('extreme_score'), self.column('PPCS_score'))
        plt.show()
