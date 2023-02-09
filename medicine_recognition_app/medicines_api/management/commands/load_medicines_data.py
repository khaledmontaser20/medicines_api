from csv import DictReader
from django.core.management import BaseCommand

# Import the model
from medicines_api.models import Medicine


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the medicines data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from data_clean.csv"

    def handle(self, *args, **options):

        # Show this if the data already exist in the database
        if Medicine.objects.exists():
            print('Medicines data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        # Show this before loading the data into the database
        print("Loading medicines data")

        # Code to load the data into database
        for row in DictReader(open('./data_clean.csv', encoding="utf8")):
            medicine = Medicine(category_name=row['category_name'], company=row['company'], effective_material=row['effective_material'],
                                en_name=row['en_name'], price=row['price'], usage=row['usage'], ar_name=row['ar_name'])
            medicine.save()
