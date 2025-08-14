from django.core.management.base import BaseCommand
from faker import Faker
from front_ronaldo.models import Profile
import random

class Command(BaseCommand):
    help = 'Seed the database with fake Profile data'

    def add_arguments(self, parser):
        parser.add_argument('--total', type=int, default=10, help='Number of profiles to create')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        for _ in range(total):
            Profile.objects.create(
                name=fake.name(),
                date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=70),
                address=fake.address(),
                zip_code=fake.postcode(),
                email=fake.email(),
                phone=fake.phone_number(),
                about_me=fake.text(max_nb_chars=200),
                image=None  # میتونی اینو با یه عکس تستی هم پر کنی
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} fake profiles'))
