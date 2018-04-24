from peewee import *

db = SqliteDatabase ('signup.db')

class Person(Model):
    id = PrimaryKeyField()
    name = CharField()
    email = CharField()
    age = IntegerField()
    statement = CharField()


    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([Person], safe=True)

initialize_db()

# here are some calls to the data I can use later

# Person.select().where((Person.name == 'leslie') & (Person.age == 30))
#
# you can use a regular for each loop, will iterate over each person in the table
# for s in Person.select()where(Person.name == 'leslie'):
    # send an email!

    # you can change values by saying
    # leslie.name = bob
    # leslie.save
    # leslie.delete_instance()
    # and you can delete people in the for each loop like this instead of sendng them an email.


 db.close()
