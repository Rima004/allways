from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.main.validators import MaxCurrentYearValidator


class Places(models.Model):
    name = models.CharField(
        max_length=500,
        verbose_name=_("Name"),
        help_text=_(
            "The official name of the place (e.g., Central Park, Joe's Diner)."
        ),
    )
    category = models.CharField(
        max_length=100,
        verbose_name=_("Category"),
        help_text=_("The type of place, such as restaurant, park, shop, etc."),
    )
    lat = models.FloatField(
        verbose_name=_("Latitude"),
        help_text=_("The geographical latitude coordinate of the place."),
    )
    lng = models.FloatField(
        verbose_name=_("Longitude"),
        help_text=_("The geographical longitude coordinate of the place."),
    )

    class Meta:
        verbose_name = _("Place")
        verbose_name_plural = _("Places")

    def __str__(self):
        return f"{self.name} [{self.category}]"


class Statistics(models.Model):
    year = models.IntegerField(
        verbose_name=_("Year"),
        help_text=_("The calendar year the data refers to."),
        validators=[
            MinValueValidator(1900),
            MaxCurrentYearValidator(),
        ],
        unique=True,
    )
    number_of_people = models.FloatField(
        verbose_name=_("Number of People (thousands)"),
        help_text=_(
            "The number of people, expressed in thousands (e.g., 2.5 = 2,500 people)."
        ),
    )

    class Meta:
        verbose_name = _("Statistics")
        verbose_name_plural = _("Statistics")

    def __str__(self):
        return f"{self.year}: {self.number_of_people}k people"
