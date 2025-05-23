# Generated by Django 4.2.20 on 2025-04-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Places",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500, verbose_name="Name")),
                ("category", models.CharField(max_length=100, verbose_name="Category")),
                ("lat", models.FloatField(verbose_name="Lat")),
                ("lng", models.FloatField(verbose_name="Lng")),
            ],
        ),
    ]
