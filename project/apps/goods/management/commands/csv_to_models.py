import csv
import os

from django.core.management import BaseCommand

from apps.goods.models import Category, PropertyObject, Product, PropertyValue


class Command(BaseCommand):
    help = "Loads data to info.csv"

    def handle(self, *args, **options):
        if not os.path.isdir('csv_models'):
            os.mkdir('csv_models')

        self.get_property_objects()
        self.get_categories()
        self.get_products()
        self.get_property_values()

    def get_property_objects(self):
        data = []

        with open('csv_models/property_objects.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(PropertyObject(**row))

        PropertyObject.objects.bulk_create(data, ignore_conflicts=True)

    def get_categories(self):
        props = {}
        data = []
        with open('csv_models/categories.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                props_ids = [i for i in row.get('properties') if i.isdigit()]
                props[int(row.get('id'))] = props_ids
                data.append(
                    Category(
                        id=row.get('id'),
                        title=row.get('title'),
                        created_at=row.get('created_at'),
                        updated_at=row.get('updated_at'),
                        slug=row.get('slug'),
                    )
                )
        Category.objects.bulk_create(data, ignore_conflicts=True)
        for key, value in props.items():
            category = Category.objects.get(id=key)
            properties = PropertyObject.objects.filter(id__in=value)
            category.properties.add(*properties)

    def get_products(self):
        data = []

        with open('csv_models/product.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(
                    Product(
                        id=row.get('id'),
                        title=row.get('title'),
                        sku=row.get('sku'),
                        created_at=row.get('created_at'),
                        updated_at=row.get('updated_at'),
                        slug=row.get('slug'),
                        category=Category.objects.get(id=int(row.get('category')))
                    )
                )

        Product.objects.bulk_create(data, ignore_conflicts=True)

    def get_property_values(self):
        products = {}
        data = []
        with open('csv_models/property_values.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                products_ids = [i for i in row.get('products') if i.isdigit()]
                products[int(row.get('id'))] = products_ids
                data.append(
                    PropertyValue(
                        id=row.get('id'),
                        code=row.get('code'),
                        type_str=row.get('type_str'),
                        property_obj=PropertyObject.objects.get(id=int(row.get('property_obj'))),
                    )
                )
        PropertyValue.objects.bulk_create(data, ignore_conflicts=True)
        for key, value in products.items():
            prop_value = PropertyValue.objects.get(id=key)
            prods = Product.objects.filter(id__in=value)
            prop_value.products.add(*prods)
