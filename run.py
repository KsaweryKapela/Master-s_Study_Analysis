from classes.visualising_results import Visualizing_Results
from functions.proccesing_raw_data import subjects_into_instances
from classes.statistical_analysis_class import StatisticalAnalysis


def main():
    tested_people = subjects_into_instances()
    stat_analysis = StatisticalAnalysis(tested_people)
    stat_analysis.print_subjects_data(0, 1)
    stat_analysis.r_pearson('PPCS_score', 'extreme_score')


if __name__ == "__main__":
    main()
