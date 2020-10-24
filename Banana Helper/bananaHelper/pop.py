import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bananaHelper.settings')

import django
django.setup()

import random
from bananaApp.models import offer
from faker import Faker

fake = Faker()

def populate(N=10):
    id_counter = 3
    for i in range(N):
        tasks = ["Wypożyczę książkę", "Nauczę Fizyki", "Pomogę w matemayce", "Zagram z tobą w ligę"]
        prices = ["10 zł/h", "20 zł/h", "15 zł/h"]

        email = fake.email()
        offer.objects.get_or_create(name=random.choice(tasks),
                                            price=random.choice(prices),
                                            offer_id = id_counter,
                                            user = email)[0]
        id_counter+=1

if __name__ == '__main__':
    print('populating please wait')
    populate()
    print('populating complete')
