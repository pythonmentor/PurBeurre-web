"""
The Database module is used to populate the database with Open Food Facts data
or delete the contents of the Product and Category table.
"""

from django.core.management.base import BaseCommand
import requests

from core.models import Category, Product
from dbmanage.config import OFF_CATS, API_CONFIG


class Command(BaseCommand):
    help = 'Database administration'

    def add_arguments(self, parser):
        parser.add_argument(
            '--populate',
            action='store_true',
            dest='populate',
            help='Populates the database with Open Food Facts data.',
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Deletes the contents of the product and category table.',
        )

    @property
    def product_count(self):
        """
        This method counts the number of products registered in the database.
        """
        return Product.objects.all().count()

    @property
    def category_count(self):
        """
        This method counts the number of categories registered in the database.
        """
        return Category.objects.all().count()

    def delete_db(self):
        """
        This method deletes the data from the Product and Category table.
        """
        self.stdout.write("Deleting the Product and Category table ...")
        self.stdout.write("Please wait ...")
        prod_count = self.product_count
        cat_count = self.category_count
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(f"-> {prod_count} products and {cat_count} categories deleted.")

    def populate_db(self):
        """
        This method populates the database with Open Food Facts data when the Product and Category tables are empty.
        If these tables are not empty, the user will be notified.
        The Open Food Facts API is used.
        """

        if self.db_is_empty():
            try:
                self.stdout.write("Saving Open Food Facts data in the local database ...")
                self.stdout.write("Please wait ...")

                # Get API configuration
                api_url = API_CONFIG["url"]
                api_criteria = API_CONFIG["criteria"]
                nutrition_grades = API_CONFIG["nutrition_grades"]
                openfoodfacts_categories = OFF_CATS["categories"]

                for category in openfoodfacts_categories:
                    api_criteria.update({"tag_0": category})

                    # Save the category in the database
                    cat = Category(name=category)
                    cat.save()

                    for nutrition_grade in nutrition_grades:
                        api_criteria.update({"tag_1": nutrition_grade})
                        # Call API
                        response = requests.get(api_url, params=api_criteria)
                        data = response.json()
                        products = data['products']

                        # Save the product in the database
                        for product in products:
                            if product.get('image_nutrition_url') and product.get('image_small_url') \
                                    and product.get('code') != "1":
                                Product(name=product.get('product_name').lower().capitalize(),
                                        code=product.get('code'),
                                        nutrition_grade=product.get('nutrition_grades'),
                                        image_nutrition_url=product.get('image_nutrition_url'),
                                        image_small_product_url=product.get('image_small_url'),
                                        image_full_product_url=product.get('image_small_url').replace('200.jpg',
                                                                                                      'full.jpg'),
                                        url=product.get('url'),
                                        category=cat).save()

                self.stdout.write("-> Database populated with Open Food Facts data.")
                self.stdout.write(f"-> {self.product_count} products and {self.category_count} "
                                  f"categories were registered.")

            except requests.exceptions.ConnectionError as err:
                # If there is an API connection problem, the Category table is flushed.
                Category.objects.all().delete()
                print(f'Error : {err}')
        else:
            self.stdout.write("Database is not empty !")
            self.stdout.write("Please use --delete before repopulating the database.")

    def db_is_empty(self):
        """
        This method checks if the Product table and the Category table are empty.
        """
        if self.product_count == 0 and self.category_count == 0:
            return True
        else:
            return False

    def handle(self, *args, **options):

        if options['populate']:
            self.populate_db()
        elif options['delete']:
            self.delete_db()
        else:
            self.stdout.write("Use one of the following options:")
            self.stdout.write(" --populate : Populates the database with Open Food Facts data.")
            self.stdout.write(" --delete : Deletes the contents of the product and category table.")
