from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Generates fake users using Faker'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  # Generar 10 usuarios de ejemplo
            username = fake.user_name()
            password = fake.password()

            user = User.objects.create_user(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f'Usuario generado: {user.username}'))
