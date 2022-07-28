import pandas as pd 

# universal store for assignments
db = './assignments.csv'

# beginning
print('\nAssignment Tracker')

# program isntructions 
instructions = "\nUse the following key bindings\n1\tA/a - add a new assignment\n2\tD/d - mark as complete\n3\tE/e - end session\n4\tL/l - list all the assignments\n\n"
print(instructions)

def add_assignment(a, b):
    '''
    add assignment takes in an assignment a 
    due date b and adds them to a csv file 

    input: assignment, due date
    output: 0 pass, 1 Fail

    return: int
    '''
    # how data is to be stored in the csv file
    data = pd.dataframe({'assignments': a, 'due date': b})

    try:
        df.to_csv(db)
        return 0
    except:
        print("invalid process adding new assignment")
        return 1
    
def more_assignments(a, b):
    '''
    add more assignments a 
    due date b and adds them to a csv file 

    input: assignment, due date
    output: 0 pass, 1 Fail

    return: int
    '''
    # the currently saved data
    
    new_assignments = pd.dataframe({'assignments': a, 'due date': b})
    