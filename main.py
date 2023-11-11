import itertools
from group_combination import GroupCombination
from helper import *

def main():
    # Get headers and person list
    headers, person_list = process_csv()

    # Hardcode number of groups, there are only 2 facilitators
    num_groups = 2
    person_per_group = len(person_list) // num_groups

    group_combinations = []

    # Create all possible combinations of people of size person_per_group
    for group in itertools.combinations(person_list, person_per_group):
        
        # Get the remaining people
        remaining_people = set(person_list) - set(group)

        group_combinations.append(GroupCombination(group, remaining_people))

    # Sort group combinations by score
    group_combinations.sort(key = lambda x: x.get_score(), reverse = True)

    # Print the first 3 group combinations
    for index in range(3):
        print(f'Proposal {index + 1}\n')
        group_combinations[index].print_groups(headers)
        print('-' * 50 + '\n')
    
    # Create a vCard for the best group combination
    create_contacts(group_combinations[0])

if __name__ == '__main__':
    main()