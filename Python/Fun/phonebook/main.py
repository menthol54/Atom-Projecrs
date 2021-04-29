#User inputs a code
user_input = input('''>> Welcome to your phonebook
>> Type 1 to create a new contact
>> Type 2 to view a contact
>> Type 3 to edit a contact
>> Type 4 to delete a contact
>> What would you like to do: ''')
contact = user_input
#Fuction one creates a contact
global person
person = {}
def create():
    if contact == '1':
        name = input('Name: ')
        num = input('Number: ')
        person.update({name : num})
        print(person)

        f = open(f'contacts\ {name}.txt', 'a')
        f.write(str(person))
        f.close()
create()

def view():
    if contact == '2':
        name = input("Name: ")
        fi = open(f'contacts\ {name}.txt', 'r')
        print(fi.read())
        fi.close()

view()


def delete():
