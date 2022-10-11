import pandas as pd
from classes.tested_person_class import TestedPerson


def subjects_into_instances():
    raw_data = pd.read_excel('data.xlsx')
    my_dataframe = pd.DataFrame(data=raw_data)
    my_dataframe = my_dataframe.reset_index()

    tested_people = []

    for index, row in my_dataframe.iterrows():
        if row['Sygnatura czasowa'] == 'Sygnatura czasowa':
            break
        tested_person = TestedPerson(row)
        tested_people.append(tested_person)
    return tested_people


def generate_index_dict(column):
    column_dict = {}

    for item in column:
        if item in column_dict:
            column_dict[item] += 1
        else:
            column_dict[item] = 1

    return column_dict
