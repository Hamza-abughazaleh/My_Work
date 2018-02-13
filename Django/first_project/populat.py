import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

#fake pop script
import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakgen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic ():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic from the entry
        top = add_topic()

        #create the fake data for the entry
        fake_url = fakgen.url()
        fake_date = fakgen.date()
        fake_name = fakgen.company()

        # create the new Webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        #create a fake AccessRecord of the Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("population script !")
    populate(20)
    print("populating complete!")
