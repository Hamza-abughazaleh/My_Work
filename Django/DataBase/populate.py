import os
from django.utils import timezone
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DataBase.settings')

import django
django.setup()

import random
from DBapp.models import UserInfo , Trip
from faker import Faker

fakgen = Faker()
#def populate(N=5):
    #for entry in range(N):
        #create the fake data for the entry
        #    username_fake = fakgen.user_name()
        #    name=fakgen.name().split()
        #    fake_fistname = name[0]
        #    fake_lastname =name[1]
        #    fake_email = fakgen.email()
        #    fake_password = fakgen.password()


        # create the new user entry
        #    user = UserInfo.objects.get_or_create(username=username_fake,firstname=fake_fistname,lastname=fake_lastname,email=fake_email,password=fake_password)[0]



UserInfo_ids = UserInfo.objects.all().values('id')
objects = UserInfo.objects.filter(id__in=UserInfo_ids)


def add_ForeignKey ():
    t=random.choice(objects)
    return t

def populate_Trip(N=1):
    for entry in range(N):
            ids = add_ForeignKey()

            fake_title = fakgen.country()
            fake_text = fakgen.text()
            fake_date = timezone.now()
            trip = Trip.objects.get_or_create(title=fake_title,userid=ids,text=fake_text,date=fake_date)[0]




if __name__ == '__main__':
#    print("population script !")
#    populate(20)
#    print("populating complete!")
     print("population script !")
     populate_Trip(5)
     print("populating complete!")
