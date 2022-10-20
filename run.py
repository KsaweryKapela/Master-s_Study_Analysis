from classes.visualising_results import Visualizing_Results
from functions.checking_hypothesis import *
from functions.functions_ import subjects_into_instances
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


def main():
    tested_people = subjects_into_instances()
    stat = StatisticalAnalysis(tested_people)
    vision = Visualizing_Results(tested_people)

    stat.spearman('reenacting_porn', 'extreme_score')
    reenacting_and_extreme_score(stat, split_into_faith_data)
    reenacting_and_extreme_score(stat, split_into_sex_data)
    reenacting_and_extreme_score(stat, split_into_relationship_data)
    reenacting_and_extreme_score(stat, split_into_well_being_data)


if __name__ == "__main__":
    main()
