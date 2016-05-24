empty_dictionary = {'Monday':[],
                    'Tuesday':[],
                    'Wednesday':[],
                    'Thursday':[],
                    'Friday':[],
                    'Saturday':[],
                    'Sunday':[]}
def add(action,day):
    # loop this question...
        #append the action to the list value of the day keys
        empty_dictionary[day].append(action)
    #until you...
    # I need an option to call choice()

def get(day):
    print empty_dictionary[day]
    # I need an option to call choice()

def choice():
    user_choice = raw_input("How can I help you?")
    if user_choice == 'add':
        action = raw_input("What would you like to do?")
        day = raw_input("What day?").capitalize()
        add(action,day)
    elif user_choice == 'get':
        action = raw_input("What would you like to do?")
        day = raw_input('What day?').capitalize()
print empty_dictionary
