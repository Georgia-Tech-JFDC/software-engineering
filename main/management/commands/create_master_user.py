from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates the master user account for JFDC'

    def handle(self, *args, **options):
        username = 'jfdc'
        password = 'GaTech$$JFDC'

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Updated existing master user "{username}"'))
        else:
            # Create new user
            User.objects.create_superuser(
                username=username,
                password=password,
                email='jfdc@gatech.edu'
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created master user "{username}"'))
