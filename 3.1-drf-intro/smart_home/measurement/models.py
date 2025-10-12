from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

    

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
   

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(max_length=None, null=True, blank=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    def __str__(self):
        return f'{self.temperature}, {self.created_at}'


    
    