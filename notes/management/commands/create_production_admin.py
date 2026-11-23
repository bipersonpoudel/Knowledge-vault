
import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create a production admin account"

    def handle(self, *args, **options):
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            raise CommandError("Production admin credentials are missing.")

        User = get_user_model()

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email},
        )

        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Production admin {'created' if created else 'updated'} successfully."
            )
        )
