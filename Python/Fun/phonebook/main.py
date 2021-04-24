# User inputs a code
user_input = input('''>> Welcome to your phonebook
>> Type 1 to create a new contact
>> Type 2 to edit a contact
>> Type 3 to view a contact
>> Type 4 to delete a contact
>> What would you like to do: ''')
contact = user_input
global person
person = {}
# Fuction one creates a contact


def create():
    if contact == '1':
        name = input('Name: ')
        num = input('Number: ')
        person.update({name: num})
        print(person)
create()

def edit():
    if contact == '2':
        pass
