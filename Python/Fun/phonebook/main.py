# User inputs a code
def enter():
    user_input = int(input('''>> Welcome to your phonebook
    >> Type 1 to create a new contact
    >> Type 2 to edit a contact
    >> Type 3 to view a contact
    >> Type 4 to delete a contact
    >> What would you like to do: '''))
    return user_input



global person
person = []
# Fuction one creates a contact


def create():
    while True:
        contact = enter()
    if contact == 1:
        name = str(input('Name: '))
        num = int(input('Number: '))
        person.append(name + ':' + str(num))
        print(person)


create()
# create a function to edit


def edit():
    if contact == '2':
        pass


def view():
    if contact == '3':
        pass
