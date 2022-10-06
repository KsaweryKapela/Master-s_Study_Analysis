from functions.proccesing_raw_data import subjects_into_instances
from classes.statistical_analysis_class import StatisticalAnalysis

tested_people = subjects_into_instances()
stat_analysis = StatisticalAnalysis(tested_people)
stat_analysis.print_subjects_data()
