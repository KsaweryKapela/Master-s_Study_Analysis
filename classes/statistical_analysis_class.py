import math

from scipy.stats import pearsonr, shapiro, mannwhitneyu


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
            if not math.isnan(attribute):
                atr_list.append(attribute)
        return atr_list

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

    def r_pearson(self, column_string_1, column_string_2, alternative='two-sided'):
        column_1 = self.column(column_string_1)
        column_2 = self.column(column_string_2)
        result = pearsonr(column_1, column_2, alternative=alternative)
        print(result)
        if result[1] < 0.05:
            print('Data is statistically significant')
        elif result[1] > 0.05:
            print('Data is not statistically significant')

    def shapiro_wilk(self, column_string):
        column = self.column(column_string)

        result = shapiro(column)
        print(result)
        return result

    def is_normal(self, column_string, alpha_level=0.05):
        if self.shapiro_wilk(column_string)[1] > alpha_level:
            return True
        else:
            return False

    def mann_whitney(self, column_string):
        male_data, female_data = self.split_column_into_sexes(column_string)
        result = mannwhitneyu(male_data, female_data)
        print(result)