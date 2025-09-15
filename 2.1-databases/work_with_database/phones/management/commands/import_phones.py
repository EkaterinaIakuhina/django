import csv
from slugify import slugify
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            with open('phones.csv', 'r', encoding='utf-8') as file:
                phones = list(csv.DictReader(file, delimiter=';'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Файл phones.csv не найден'))

        try:
            for phone in phones:
                # TODO: Добавьте сохранение модели
                new_phone = Phone(
                    name=phone.get('name'),
                    price=Decimal(phone.get('price')),
                    image=phone.get('image'),
                    release_date=phone.get('release_date'),
                    lte_exists=phone.get('lte_exists', False),
                    slug = slugify(phone.get('name'))
                )
                
                new_phone.save()

        except IntegrityError:
            self.stdout.write(self.style.ERROR('Ошибка при добавлении дубликата'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при добавлении записей в бд: {e}'))
