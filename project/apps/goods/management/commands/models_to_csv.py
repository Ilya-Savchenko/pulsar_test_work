import csv
import os

from django.core.management import BaseCommand

from apps.goods.models import Product, Category, PropertyObject, PropertyValue


class Command(BaseCommand):
    help = "Loads data to info.csv"

    def write_products(self):
        fieldnames = [fieldname.name for fieldname in Product._meta.fields]
        products = Product.objects.all()
        rows = []
        for product in products:
            rows.append(
                {
                    'id': product.id,
                    'title': product.title,
                    'sku': product.sku,
                    'slug': product.slug,
                    'category': product.category.id,
                    'updated_at': product.updated_at,
                    'created_at': product.created_at,
                }
            )

        with open('csv_models/product.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def write_property_objects(self):
        fieldnames = [fieldname.name for fieldname in PropertyObject._meta.fields]
        objects = PropertyObject.objects.all()
        rows = []
        for obj in objects:
            rows.append(
                {
                    'id': obj.id,
                    'title': obj.title,
                    'code': obj.code,
                    'type': obj.type,
                    'updated_at': obj.updated_at,
                    'created_at': obj.created_at,
                }
            )

        with open('csv_models/property_objects.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def write_property_values(self):
        fieldnames = [fieldname.name for fieldname in PropertyValue._meta.fields]
        fieldnames.append('products')
        values = PropertyValue.objects.all()
        rows = []
        for value in values:
            rows.append(
                {
                    'id': value.id,
                    'type_str': value.type_str,
                    'type_number': value.type_number,
                    'code': value.code,
                    'property_obj': value.property_obj.id,
                    'products': [obj.id for obj in value.products.only('id')],
                }
            )

        with open('csv_models/property_values.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def write_categories(self):
        fieldnames = [fieldname.name for fieldname in Category._meta.fields]
        fieldnames.append('properties')
        categories = Category.objects.all()
        rows = []
        for category in categories:
            rows.append(
                {
                    'id': category.id,
                    'title': category.title,
                    'slug': category.slug,
                    'properties': [obj.id for obj in category.properties.only('id')],
                    'updated_at': category.updated_at,
                    'created_at': category.created_at,
                }
            )

        with open('csv_models/categories.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def handle(self, *args, **options):
        if not os.path.isdir('csv_models'):
            os.mkdir('csv_models')

        self.write_products()
        self.write_property_objects()
        self.write_property_values()
        self.write_categories()
