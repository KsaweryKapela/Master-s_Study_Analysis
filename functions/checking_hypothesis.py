def weekly_minutes_and_sexual_life(stat_class_instance, split_method):
    string = 'Weekly minutes/ sexual life satisfaction correlation'
    split_method(stat_class_instance, 'weekly_minutes', 'sexual_life', string)


def frequency_and_sexual_life(stat_class_instance, split_method):
    string = 'Weekly sessions/ sexual life satisfaction correlation'
    split_method(stat_class_instance, 'weekly_sessions', 'sexual_life', string)


def extreme_score_and_sexual_life(stat_class_instance, split_method):
    string = 'Extreme pornography score/ sexual life satisfaction correlation'
    split_method(stat_class_instance, 'extreme_score', 'sexual_life', string)


def extreme_score_and_PPCS_score(stat_class_instance, split_method):
    string = 'Extreme pornography score/ PPCS scores'
    split_method(stat_class_instance, 'extreme_score', 'PPCS_score', string)


def more_and_more_hardcore_and_sexual_life(stat_class_instance, split_method):
    string = 'Extreme pornography score/ sexual life satisfaction correlation'
    split_method(stat_class_instance, 'more_and_more_hardcore', 'sexual_life', string)


def releasing_tension_and_sexual_life(stat_class_instance, split_method):
    string = 'Sexual satisfaction/ releasing tension with pornography correlation'
    split_method(stat_class_instance, 'releasing_tension', 'sexual_life', string)


def releasing_tension_and_extreme_score(stat_class_instance, split_method):
    string = 'Extreme score/ releasing tension with pornography correlation'
    split_method(stat_class_instance, 'releasing_tension', 'extreme_score', string)


def reenacting_and_sexual_life(stat_class_instance, split_method):
    string = 'Sexual satisfaction/ reenacting pornography in real life correlation'
    split_method(stat_class_instance, 'reenacting_porn', 'sexual_life', string)


def reenacting_and_releasing_tension(stat_class_instance, split_method):
    string = 'Releasing tension with pornography/ reenacting pornography in real life correlation'
    split_method(stat_class_instance, 'reenacting_porn', 'releasing_tension', string)


def reenacting_and_extreme_score(stat_class_instance, split_method):
    string = 'Extreme score/ reenacting pornography in real life correlation'
    split_method(stat_class_instance, 'extreme_score', 'reenacting_porn', string)


def frequency_and_romantic_life(stat_class_instance, split_method):
    string = 'Weekly minutes/ romantic life satisfaction correlation'
    split_method(stat_class_instance, 'weekly_minutes', 'romantic_life', string)


def extreme_score_and_romantic_life(stat_class_instance, split_method):
    string = 'Extreme pornography score/ romantic life satisfaction correlation'
    split_method(stat_class_instance, 'extreme_score', 'romantic_life', string)


def split_into_sex_data(stat_class_instance, string_1, string_2, correlation_string):
    male_data, female_data = stat_class_instance.split_column_into_sexes(string_1)
    male_data_2, female_data_2 = stat_class_instance.split_column_into_sexes(string_2)

    print(correlation_string, '\n')
    print('male data:')
    stat_class_instance.spearman(male_data, male_data_2)
    print('\nfemale data:')
    stat_class_instance.spearman(female_data, female_data_2)
    print('\n')


def split_into_faith_data(stat_class_instance, string_1, string_2, correlation_string):
    male_data, female_data = stat_class_instance.split_column_faith(string_1)
    male_data_2, female_data_2 = stat_class_instance.split_column_faith(string_2)

    print(correlation_string, '\n')
    print('Believers data:')
    stat_class_instance.spearman(male_data, male_data_2)
    print('\nAtheist data:')
    stat_class_instance.spearman(female_data, female_data_2)
    print('\n')


def split_into_relationship_data(stat_class_instance, string_1, string_2, correlation_string):
    male_data, female_data = stat_class_instance.split_column_into_relationship_status(string_1)
    male_data_2, female_data_2 = stat_class_instance.split_column_into_relationship_status(string_2)

    print(correlation_string, '\n')
    print('In relationship data:')
    stat_class_instance.spearman(male_data, male_data_2)
    print('\nSingle data:')
    stat_class_instance.spearman(female_data, female_data_2)
    print('\n')


def split_into_well_being_data(stat_class_instance, string_1, string_2, correlation_string):
    male_data, female_data = stat_class_instance.split_column_into_well_being(string_1)
    male_data_2, female_data_2 = stat_class_instance.split_column_into_well_being(string_2)

    print(correlation_string, '\n')
    print('Felt bad in last 6 months:')
    stat_class_instance.spearman(male_data, male_data_2)
    print('\nFelt good:')
    stat_class_instance.spearman(female_data, female_data_2)
    print('\n')