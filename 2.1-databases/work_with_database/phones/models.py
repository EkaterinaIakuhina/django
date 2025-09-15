from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=40, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=1)
    image = models.ImageField()
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField()
    slug = models.SlugField()


    def __str__(self):
        return f'{self.id}: {self.name}'

