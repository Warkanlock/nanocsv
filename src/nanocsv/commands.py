class Command:
    pass

class AddRow(Command):
    def __init__(self, values):
        self.values = values

class RemoveRow(Command):
    def __init__(self, row_number):
        self.row_number = row_number

class SearchRow(Command):
    def __init__(self, conditions):
        self.conditions = conditions
