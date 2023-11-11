class Person:

    def __init__(self, row):

        # First column is timestamp in google forms

        # 2nd and 3rd columns are name and phone number
        self.name = row[1]
        self.phone_number = row[2]

        # Preferences is all the columns after the first two
        self.preferences = row[3:]

    # Override print function
    def __str__(self):
        return f'{self.name}'

    def get_preferences(self):
        # Convert preferences to integers
        preferences = [int(preference) for preference in self.preferences]
        return preferences