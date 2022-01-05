from django.core.management.base import BaseCommand
from solaris.models import TableCell


class Command(BaseCommand):
    def handle(self, *args, **options):
        cells = TableCell.objects.filter(row=0)
        for cell in cells:
            cell.thead = True
            cell.save()
