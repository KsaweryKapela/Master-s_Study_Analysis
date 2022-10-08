from scipy.stats import pearsonr, shapiro


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
        result = pearsonr(column_1, column_2, alternative='greater')
        print(result)

    def shapiro_wilk(self, column_string):
        column = self.column(column_string)
        result = shapiro(column)
        print(result)
        return result

    def is_normal(self, column_string):
        if self.shapiro_wilk(column_string)[0] > 0.05:
            return True
        else:
            return False
