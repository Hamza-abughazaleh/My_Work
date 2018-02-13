import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","third_project.settings")

import django
django.setup()

from third_app.models import Users
from faker import Faker

fakgen = Faker()
def populate(N=5):
    for entry in range(N):

        #create the fake data for the entry
        name=fakgen.name().split()
        fake_fistname = name[0]
        fake_lastname =name[1]
        fake_email = fakgen.email()

        user = Users.objects.get_or_create(first_name=fake_fistname,last_name=fake_lastname,email=fake_email)[0]

if __name__ == '__main__':
    print("population script !")
    populate(20)
    print("populating complete!")
