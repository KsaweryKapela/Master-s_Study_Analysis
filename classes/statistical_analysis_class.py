import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr


class StatisticalAnalysis:
    def __init__(self, subjects):
        self.subjects = subjects

    def print_subjects_data(self, start_index=0, end_index=None):
        for subject in self.subjects[start_index: end_index]:
            subject.print_persons_data()

    def column(self, attribute_name):
        atr_list = []
        for row in self.subjects:
            attribute = getattr(row, attribute_name)
            atr_list.append(attribute)
        return atr_list

    def r_pearson(self, column_string_1, column_string_2):
        column_1 = self.column(column_string_1)
        column_2 = self.column(column_string_2)
        result = pearsonr(column_1, column_2)
        print(result)
