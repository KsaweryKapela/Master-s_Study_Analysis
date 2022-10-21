import math

import numpy as np
from matplotlib import pyplot as plt
from sklearn import preprocessing
from scipy.stats import pearsonr, shapiro, mannwhitneyu, spearmanr, linregress


class StatisticalAnalysis:
    def __init__(self, subjects):
        self.subjects = subjects

    def print_subjects_data(self, start_index=0, end_index=None):
        for subject in self.subjects[start_index: end_index]:
            subject.print_persons_data()

    def column(self, attribute_name):
        if type(attribute_name) == str:
            atr_list = []
            for row in self.subjects:
                attribute = getattr(row, attribute_name)
                if not math.isnan(attribute):
                    atr_list.append(attribute)
        else:
            atr_list = attribute_name
        return atr_list

    def split_column_faith(self, attribute_name):
        believers_data = []
        atheist_data = []
        for row in self.subjects:
            attribute = getattr(row, attribute_name)
            if not math.isnan(attribute):
                if row.believes_in_god:
                    believers_data.append(attribute)
                elif not row.believes_in_god:
                    atheist_data.append(attribute)
        return believers_data, atheist_data

    def split_column_into_sexes(self, attribute_name):
        male_data = []
        female_data = []
        for row in self.subjects:
            attribute = getattr(row, attribute_name)
            if not math.isnan(attribute):
                if row.sex == 0:
                    female_data.append(attribute)
                elif row.sex == 1:
                    male_data.append(attribute)
        return male_data, female_data

    def split_column_into_relationship_status(self, attribute_name):
        single_data = []
        in_relationship = []
        for row in self.subjects:
            attribute = getattr(row, attribute_name)
            if not math.isnan(attribute):
                if row.single:
                    single_data.append(attribute)
                elif not row.single:
                    in_relationship.append(attribute)
        return in_relationship, single_data

    def split_column_into_well_being(self, attribute_name):
        bad_well_being = []
        good_well_being = []
        for row in self.subjects:
            attribute = getattr(row, attribute_name)
            if not math.isnan(attribute):
                if row.well_being <= 5:
                    bad_well_being.append(attribute)
                elif row.well_being > 5:
                    good_well_being.append(attribute)

        return bad_well_being, good_well_being

    def r_pearson(self, column_string_1, column_string_2, alternative='two-sided'):
        column_1 = self.column(column_string_1)
        column_2 = self.column(column_string_2)

        result = pearsonr(column_1, column_2, alternative=alternative)
        print(result)

    def spearman(self, column_string_1, column_string_2):

        if type(column_string_1) == str:
            column_1 = self.column(column_string_1)

        else:
            column_1 = column_string_1

        if type(column_string_2) == str:
            column_2 = self.column(column_string_2)
        else:
            column_2 = column_string_2

        result = spearmanr(column_1, column_2)
        print(f'n={len(column_1)}')
        print(result)

    def shapiro_wilk(self, column_string):
        column = self.column(column_string)

        result = shapiro(column)
        return result

    def is_normal(self, column_string, alpha_level=0.05):
        if self.shapiro_wilk(column_string)[1] > alpha_level:
            return True
        else:
            return False

    def normalize(self, column_string):
        column_data = self.column(column_string)
        column_data = np.array(column_data).reshape(-1, 1)
        scaler = preprocessing.StandardScaler().fit(column_data)
        column_data_scaled = scaler.transform(column_data)

        normalized_column = []
        for data in column_data_scaled:
            normalized_column.append(*data)

        return normalized_column

    def mann_whitney(self, column_string):
        male_data, female_data = self.split_column_into_sexes(column_string)
        result = mannwhitneyu(male_data, female_data, alternative='less')
        print(result)

    def linear_regression(self, column_string_1, column_string_2):
        if type(column_string_1) == str:
            column_1 = self.column(column_string_1)

        else:
            column_1 = column_string_1

        if type(column_string_2) == str:
            column_2 = self.column(column_string_2)
        else:
            column_2 = column_string_2

        result = linregress(column_1, column_2)
        print(result)