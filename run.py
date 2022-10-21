import numpy as np

from classes.visualising_results import Visualizing_Results
from functions.checking_hypothesis import *
from functions.functions_ import subjects_into_instances, delete_edge_case
from classes.statistical_analysis_class import StatisticalAnalysis

# weekly_minutes_and_sexual_life(stat, split_into_faith_data)

# frequency_and_romantic_life(stat, split_into_sex_data)

# stat.spearman('reenacting_porn', 'extreme_score')
# reenacting_and_extreme_score(stat, split_into_relationship_data)
# reenacting_and_extreme_score(stat, split_into_well_being_data)

# stat.spearman('reenacting_porn', 'releasing_tension')
# reenacting_and_releasing_tension(stat, split_into_well_being_data)
# reenacting_and_releasing_tension(stat, split_into_faith_data)
# reenacting_and_releasing_tension(stat, split_into_sex_data)


# stat.spearman('extreme_score', 'releasing_tension')
# releasing_tension_and_extreme_score(stat, split_into_relationship_data)
# releasing_tension_and_extreme_score(stat, split_into_faith_data)
# releasing_tension_and_extreme_score(stat, split_into_sex_data)


# stat.spearman('weekly_sessions', 'sexual_life')
# frequency_and_sexual_life(stat, split_into_faith_data)

# extreme_score_and_romantic_life(stat, split_into_relationship_data)


def run():
    tested_people = subjects_into_instances()
    stat = StatisticalAnalysis(tested_people)
    vision = Visualizing_Results(tested_people)
    extreme_score_and_PPCS_score(stat, split_into_sex_data)
    extreme_score_and_PPCS_score(stat, split_into_faith_data)
    extreme_score_and_PPCS_score(stat, split_into_relationship_data)
    extreme_score_and_PPCS_score(stat, split_into_well_being_data)


def run_without_edge_cases():
    tested_people = subjects_into_instances()
    for person in tested_people[:]:
        if person.weekly_minutes > 300:
            tested_people.remove(person)

    stat = StatisticalAnalysis(tested_people)

    vision = Visualizing_Results(tested_people)
    extreme_raw = stat.column('extreme_score')
    extreme_rounded = [(round(value * 2) / 2) for value in extreme_raw]

    transform_extreme = np.log(extreme_rounded)
    transform_extreme = (list(transform_extreme))

    ppcs_score = stat.column('PPCS_score')
    transform_ppcs = np.log(ppcs_score)
    transform_ppcs = list(transform_ppcs)
    # vision.bar_graph(ppcs_score)
    vision.bar_graph(transform_extreme)
    vision.scatter_plot(transform_ppcs, transform_extreme)
    vision.scatter_plot('extreme_score', 'PPCS_score')


if __name__ == "__main__":
    run_without_edge_cases()
    # main()
