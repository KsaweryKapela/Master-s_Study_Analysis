from classes.visualising_results import Visualizing_Results
from functions.proccesing_raw_data import subjects_into_instances
from classes.statistical_analysis_class import StatisticalAnalysis


def main():
    tested_people = subjects_into_instances()
    stat = StatisticalAnalysis(tested_people)
    # vision = Visualizing_Results(tested_people)
    # vision.bar_graph('believes_in_god')
    if stat.is_normal('NEET'):
        print('x')
        stat.shapiro_wilk('NEET')
    #
    # stat.r_pearson('PPCS_score', 'extreme_score')


if __name__ == "__main__":
    main()
