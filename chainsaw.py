"""
A menu - you need to add the database and fill in the functions. 
"""
from peewee import *

db = SqliteDatabase('chainsaws.sqlite')

class Chainsawists(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = database
    
    def _str_(self):
        return f'{self.id}: {self.name}, {self.country}, {self.age}'


def main():

    create_table()

    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            Chainsawists.delete().execute() # clear the database for next time
            break
        else:
            print('Not a valid selection, please try again')

def create_table():
    
    db.connect()
    db.create_tables([Chainsawists])

    janne = Chainsawists(name='Janne Mustonen', country='Finland', catches=98)
    janne.save()

    ian = Chainsawists(name='Ian Stewart', country='Canada', catches=94)
    ian.save()

    aaron = Chainsawists(name='Aaron Gregg', country='Canada', catches=88)
    aaron.save()

    chad = Chainsawists(name='Chad Taylor', country='USA', catches=78)
    chad.save()

def display_all_records():
    # print('todo display all records')
    for chainsawist in Chainsawists.select():
        print(chainsawist)


def add_new_record():
    # might add user input validation method
    # print('todo add new record. What if user wants to add a record that already exists?')
    new_name = input('What is the chainsawist\'s name? ')
    name_from_db = Chainsawists.get_or_none(name=new_name)
    if name_from_db:
        print('Sorry, that person is already in the database')
        return
    else:
        country = input('From which country is the chainsawist? ')
        catches = input('How many catches did they have? ')

def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?') 


def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?') 


if __name__ == '__main__':
    main()