from classes.visualising_results import Visualizing_Results
from functions.functions_ import subjects_into_instances
from classes.statistical_analysis_class import StatisticalAnalysis


def main():
    tested_people = subjects_into_instances()
    stat = StatisticalAnalysis(tested_people)
    vision = Visualizing_Results(tested_people)

    stat.shapiro_wilk('mother_relations')
    # vision.sex_double_graph_bar('more_and_more_hardcore', 7)


if __name__ == "__main__":
    main()
