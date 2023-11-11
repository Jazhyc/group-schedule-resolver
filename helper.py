import csv
from person import Person

GROUP_NAME = "AISF 2023 Cohort"

# Returns a processed string which only contains the meeting day and time
def process_header(text):

    MEETING_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    meeting_day = None
    # Get the meeting day from the text
    for day in MEETING_DAYS:
        if day in text:
            meeting_day = day
            break
    
    # Get the meeting time from the text enclosed in []
    meeting_time = text[text.find('[') + 1:text.find(']')]

    return f'{meeting_day} {meeting_time}'

# Opens the csv and obtain headers and list of persons
def process_csv():

    # Open and read csv file
    with open('responses.csv', 'r') as csv_file:
        
        # Create reader
        csv_reader = csv.reader(csv_file)

        # Get headers
        raw_headers = next(csv_reader)

        # Remove first three columns from headers
        headers = [process_header(header) for header in raw_headers[3:]]

        person_list = []

        # Create a list of Person objects
        for row in csv_reader:
            person_list.append(Person(row))

    return headers, person_list

# Create a csv file to store the contacts
def create_contacts(combination):
    
    # Create a csv file which stores the name and phone number of each person
    with open('contacts.csv', 'w', newline='') as csv_file:
        
        # Create writer and write headers
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Name', 'Phone Number'])

        # Loop over groups
        groups = combination.get_groups()
        for index in range(len(groups)):
            
            group = groups[index]

            # Loop over people in group
            for person in group.get_group():
                csv_writer.writerow([f'{GROUP_NAME} {index + 1} {person.name}', person.phone_number])
                