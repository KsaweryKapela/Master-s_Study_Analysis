from pprint import PrettyPrinter


class TestedPerson:
    def __init__(self, data):
        self.data = data

        self.index = data['index']
        self.extreme_score = round(data['Extreme score podzielony'], 2)
        self.PPCS_score = data['SUMA PPCS:']

        self.well_beeing = data['Samopoczucie']
        self.mother_relations = data['Relacja z matką']
        self.father_relations = data['Relacja z ojcem']
        self.friends_relations = data['Relacja z przyjaciółmi']
        self.romantic_life = data['Życie romantyczne']
        self.sexual_life = data['Życie seksualne']

        self.more_and_more_hardcore = data[more_and_more_question_string]
        self.reenacting_porn = data['Odtwarzanie scen z porno']
        self.weekly_sessions = data['Tygodniowa częstotliwość']
        self.time_of_session = data['Czas trwania sesji']
        self.weekly_minutes = self.weekly_sessions * self.time_of_session

        self.sex = self.return_sex()
        self.age = data['Wiek']
        self.NEET = self.return_NEET()
        self.single = self.return_single()
        self.believes_in_god = self.return_faith_status()
        self.goes_to_church = self.return_church_status()

    def return_faith_status(self):
        if self.data['Wiara'] == 'Nie':
            return False
        else:
            return True

    def return_church_status(self):
        if self.data['Wiara'] in ['Tak, ale nie praktykującą', 'Nie']:
            return False
        else:
            return True

    def return_sex(self):
        sex_string = self.data['Płeć']
        if sex_string == 'Kobieta':
            return 0
        elif sex_string == 'Mężczyzna':
            return 1
        else:
            return None

    def return_single(self):
        if self.data['Status związku'] == 'Singiel/singielka':
            return True
        else:
            return False

    def return_NEET(self):
        if self.data['Zajęcie'] == 'Żadne z powyższych':
            return True
        else:
            return False

    def print_persons_data(self):
        tested_person_dict = {
            self.index: {
                'Questionnaires scores': {
                    'Extreme score': self.extreme_score,
                    'PPCS score': self.PPCS_score,
                },
                'Well-being scores': {
                    'Well-being': self.well_beeing,
                    'Mother relations': self.mother_relations,
                    'Father relations': self.father_relations,
                    'Friends relations': self.friends_relations,
                    'Romantic life': self.romantic_life,
                    'Sexual life': self.sexual_life,
                },
                'Porn oriented data': {
                    'More and more hardcore': self.more_and_more_hardcore,
                    'Reenacting porn': self.reenacting_porn,
                    'Weekly sessions': self.weekly_sessions,
                    'Time of session': self.time_of_session,
                    'Weekly minutes': self.weekly_minutes,
                },
                'Person data': {
                    'Sex': self.sex,
                    'Age': self.age,
                    'Is NEET': self.NEET,
                    'Is single': self.single,
                    'Believes in god': self.believes_in_god,
                    'Goes to church': self.goes_to_church
                }
            }
        }

        pprint = PrettyPrinter()
        pprint.pprint(tested_person_dict)

    def __str__(self):
        return f'Tested person {self.index}'


more_and_more_question_string = '7. Stopniowo oglądałem/am bardziej „ekstremalną” pornografię, ponieważ ta, ' \
                                'którą oglądałem/am wcześniej, stawała się mniej satysfakcjonująca.'
