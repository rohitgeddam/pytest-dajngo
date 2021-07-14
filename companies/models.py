from django.db import models


# Create your models here.
from django.utils.timezone import now


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(
        max_length=25, choices=CompanyStatus.choices, default=CompanyStatus.HIRING
    )
    latest_updated = models.DateTimeField(default=now, editable=True)
    application_link = models.URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
