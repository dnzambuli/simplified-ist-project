import pandas as pd 

# universal store for assignments
db = './assignments.csv'

# functions for the program
def add_assignment(a, b):
    '''
    add assignment takes in an assignment a 
    due date b and adds them to a csv file 

    input: assignment, due date
    output: 0

    return: int
    '''
    # how data is to be stored in the csv file
    data = pd.dataframe({'assignments': a, 'due date': b})

    try:
        df.to_csv(db)
    except:
        raise Exception("invalid process adding new assignment")
    else:
        return 0
    
def more_assignments(a, b):
    '''
    more_assignments takes new assignments a and
    new due date b and adds them to a csv file 

    input: assignment, due date
    output: none

    return: 0 or Error
    '''
    # the currently saved data
    curr_assignments = pd.read_csv(db)

    # the new assignments to be added 
    new_assignments = pd.dataframe({'assignments': a.title(), 'due date': b})

    # adding the new assignment to the existing ones
    try:
        curr_assignments.append(new_assignments, ignore_index=0)
    except:
        raise Exception("invalid input")
    else:
        return 0


def delete_assignment(a):
    '''
    delete_assignments takes the assignment name and deletes it from the database

    return 0
    '''
    # store the dataset to be deleted from
    data_to_delete = pd.read_csv(db, index_col = 'assignments')

    # catch when the name doesn't exist
    try:
        assignment = a.title()
        data_to_delete.drop(assignment, inplace=True)
    except:
        raise Exception("\n\tNo Such Data\n\t")
    else:
        return 0
    
