from django.db import models


class UserSubmission(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.phone}"