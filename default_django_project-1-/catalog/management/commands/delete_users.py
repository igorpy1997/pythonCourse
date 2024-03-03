from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Delete users with specified IDs"

    def add_arguments(self, parser):
        parser.add_argument("user_ids", nargs="+", type=int, help="List of user IDs to delete")

    def handle(self, *args, **options):
        deleted_count = 0
        users_queryset = User.objects.filter(pk__in="user_ids")

        if users_queryset.filter(is_superuser=True).exists():
            self.stdout.write(self.style.ERROR("ERROR:superuser can't deleted"))
        else:
            deleted_count, _ = users_queryset.delete()
        self.stdout.write(self.style.SUCCESS(f"Successfully deleted {deleted_count} users"))
