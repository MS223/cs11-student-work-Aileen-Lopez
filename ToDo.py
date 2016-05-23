action = raw_input("What would you like to do?")
day = raw_input("What day?")
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
        some_dictionary[day].append(action)
    #until you...
    # I need an option to call choice()

def get(day):
    print some_dictionary[day]
    # I need an option to call choice()

def choice():
    user_choice = raw_input("How can I help you?")
    # if they choose 'add' call add()
    # if they choose 'get' call get()
add("something", "monday")

get("monday")

# days_of_week[day] = action
# print days_of week
