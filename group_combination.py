from group import Group

class GroupCombination:

    def __init__(self, group1, group2):
        
        self.groups = [Group(group1), Group(group2)]

    # Prints meeting time along with the group and its score
    # Requires the headers from the csv file
    def print_groups(self, headers):

        # Loop over groups and print them
        for index in range(len(self.groups)):
            print(f'{headers[self.groups[index].index]}')
            print(f'Group {index + 1}, Score = {self.groups[index].score}')
            print(self.groups[index])
        
    # Create comparison function for sorting
    def get_score(self):
        return sum(group.score for group in self.groups)
    
    def get_groups(self):
        return self.groups