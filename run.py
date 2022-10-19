from classes.visualising_results import Visualizing_Results
from functions.functions_ import subjects_into_instances
from classes.statistical_analysis_class import StatisticalAnalysis

def delete_edge_case(column, number):
    for item in column[:]:
        if item > number:
            column.remove(item)
    return column



def main():
    tested_people = subjects_into_instances()
    stat = StatisticalAnalysis(tested_people)
    vision = Visualizing_Results(tested_people)

    stat.spearman('extreme_score', 'sexual_life')


if __name__ == "__main__":
    main()
