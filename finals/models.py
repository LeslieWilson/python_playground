from peewee import *
from flask_peewee.rest import RestAPI
from flask_app import *
import datetime


db = SqliteDatabase ('almond.db')


# class Person(Model):
#     id = PrimaryKeyField()
#     name = CharField()
#     email = CharField()
#     age = IntegerField()
#     statement = CharField()

class Entry(Model):
    id = PrimaryKeyField()
    name = CharField()
    email = CharField()
    date = DateTimeField(default = datetime.datetime.now)
    country = CharField()
    state= CharField()
    city = CharField()
    zip = IntegerField()

    class Meta:
        database = db

def initialize_db():
    db.connect()
    db.create_tables([Entry], safe=True)

initialize_db()
# register our models so they are exposed via /api/<model>/
api = RestAPI(app)
api.register(Entry)

# configure the urls
api.setup()



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
