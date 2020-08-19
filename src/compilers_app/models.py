from django.db import models

class Program(models.Model):
    document = models.FileField(upload_to='documents/',
        db_column="image",
        null=True,
        blank=True,
    )
