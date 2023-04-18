from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


CATEGORY = (
    ('Простые','Простые'),
    ('Бюджетные','Бюджетные'),
    ('Высокого класса','Высокого класса'),
    ('Премиум класса','Премиум класса'),
    ('Элитные','Элитные')
)


class Phone(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='')
    video = models.URLField()
    cost = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    model_phone = models.CharField(choices=CATEGORY, max_length=255)


    def __str__(self):
        return self.title