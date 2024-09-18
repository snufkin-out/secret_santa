import csv
import dataclasses
import random


@dataclasses.dataclass
class Participant:
    """
    Class for Participants which want to attend.
    
    params:
        name(str): name of the participant
        email(str): email address of the participant
        gifts(str): name of another participant. e.g John gifts Peter -> John has to buy Peter a present!
    """
    name: str
    email: str
    gifts: str = "Not assigned yet"


# TODO improve this. Maybe via some website or GUI
def get_participants(file_name):
    """
    Read .csv file (file of participants) and store as Participant in participant_list. 

        .csv expected format:
            <name>, <email>
        
        params: 
            file_name: csv file to read

        returns: 
            list of participants read from the file.
    """
    participant_list = []

    with open(file_name, mode="r") as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            participant_list.append(Participant(name=lines[0], email=lines[1]))

    return participant_list


def hocus_pocus(list_of_participants):
    """
    Assign each participant a gift recipient while ensuring no one gifts themselves, 
    no mutual gifting, and no one is gifted twice.

        params:
            list_of_participants: list of users who want to participate
    """

    shuffled_list = list_of_participants.copy()
    random.shuffle(shuffled_list)

    for i, user in enumerate(list_of_participants):

        # don't allow assignment to oneself
        if user.name == shuffled_list[i].name:

            # swap with the next one in the list
            # % len ensures circular swap -> if i is last index, it wraps around to beginning of the list -> NECESSSARY to prevent out of bounds error when swapping last person
            swap_index = (i + 1) % len(shuffled_list)

            # actual swap
            shuffled_list[i], shuffled_list[swap_index] = shuffled_list[swap_index], shuffled_list[i]
    
    # assign shuffled participants as the gift recipients
    for i, user in enumerate(list_of_participants):
        user.gifts = shuffled_list[i].name
            


initial_list = get_participants("participants.csv")
# print(f"INITIAL LIST:\n {initial_list}\n\n - \n")

hocus_pocus(initial_list)
# print(f"\n - \n\nInitial list AFTER hocus pocus:\n {initial_list}\n\n\n")

for user in initial_list:
    print(f"{user.name} -> {user.gifts}")

