"""
A menu - you need to add the database and fill in the functions. 
"""
from peewee import *

db = SqliteDatabase('chainsaws.sqlite')

class Chainsawists(Model):
    name = CharField() # unique = true
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db
    
    def __str__(self):
        return f'{self.id}: {self.name}, {self.country}, {self.catches}'


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
    for c in Chainsawists.select():
        print(c)


def add_new_record():
    add_name = input('What is the chainsawist\'s name? ')
    name_from_db_check = Chainsawists.get_or_none(name=add_name) 
    if name_from_db_check:
        print('Sorry, that person is already in the database')
        return
    else:
        add_country = input('From which country is the chainsawist? ')
        add_catches = input('How many catches did they have? ')
    add_entry = Chainsawists(name=add_name, country=add_country, catches=add_catches)
    add_entry.save()

def edit_existing_record():
    display_all_records()
    edit_record_id = int(input('What is the number of the record you want to edit? '))
    id_from_db_check = Chainsawists.get_or_none(id=edit_record_id)
    if not id_from_db_check:
        print('Sorry, there\'s no record that matches that number')
        return
    else:
        edit_catches = int(input('What is the new number of catches? '))
        Chainsawists.update(catches = edit_catches).where(Chainsawists.id == edit_record_id).execute()

def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?') 
    display_all_records()
    delete_record_id = int(input('What is the number of the record you want to delete? '))
    id_from_db_check = Chainsawists.get_or_none(id=delete_record_id)
    if not id_from_db_check:
        print('Sorry, there\'s no record that matches that number')
        return
    else:
        Chainsawists.delete().where(Chainsawists.id == delete_record_id).execute()


if __name__ == '__main__':
    main()