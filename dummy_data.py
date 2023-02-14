import os , django
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
django.setup()

from faker import Faker
import random
from product.models import Product , Brand


def seed_brand(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg']
    for _  in range(n):
        name = fake.name()
        image = f"brand/{images[random.randint(0,5)]}"
        Brand.objects.create(name = name,image = image)

def seed_product(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg']
    flag_type = ['Sales','Feature','New']

    for _ in range(n):
        name =fake.name()
        sku = random.randint(1,100000)
        image = f"products/{images[random.randint(0,9)]}"
        brand = Brand.objects.get(id=random.randint(3,30))
        price = round(random.uniform(20.99,99.99),2)
        flag = flag_type[random.randint(0,2)]
        subtitle = fake.text(max_nb_chars = 500)
        description = fake.text(max_nb_chars = 2000)
        quantity = random.randint(2,50)

        Product.objects.create(
            name = name,
            image = image,
            flag = flag,
            price = price,
            sku = sku,
            brand = brand,
            subtitle = subtitle,
            description = description,
            quantity = quantity

        )


# seed_brand(30)
# seed_product(10000)