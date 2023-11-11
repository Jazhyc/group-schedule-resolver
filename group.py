class Group:

    def __init__(self, group):
        self.group = group
        self.score, self.index = self.compute_score(self.group)
    
    def get_group(self):
        return self.group
    
    # Static function to compute score of a group
    @staticmethod
    def compute_score(group):

        # Get all preferences of people in group
        preferences = [person.get_preferences() for person in group]

        # Flatten preferences by computing sum of each column, 
        # if any column contains 1, then the sum of that column will be 1
        # 1 represents inavailability for the meeting
        columns = []

        for i in range(len(preferences[0])):

            sum = 0

            for index in range(len(group)):
                sum += preferences[index][i]

                if preferences[index][i] == 1:
                    sum = 0
                    break
            
            columns.append(sum)
        
        # Get score and index of the column with the highest score
        score = max(columns)
        index = columns.index(score)
    
        return score, index

    def __str__(self):

        for person in self.group:
            print(person)

        return ''