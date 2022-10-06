class StatisticalAnalysis:
    def __init__(self, subjects):
        self.subjects = subjects

    def print_subjects_data(self, start_index=0, end_index=None):
        for subject in self.subjects[start_index: end_index]:
            subject.print_persons_data()
