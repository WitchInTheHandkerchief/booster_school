# Generated by Django 5.0.1 on 2024-02-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Events",
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
                ("name", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="event_images/")),
                (
                    "extended_image",
                    models.ImageField(upload_to="extended_event_images/"),
                ),
                ("datetime", models.DateTimeField()),
                ("duration", models.CharField(max_length=255)),
                ("speaker_name", models.CharField(max_length=255)),
                ("free_spots", models.IntegerField()),
            ],
            options={
                "verbose_name": "event",
                "verbose_name_plural": "events",
            },
        ),
    ]