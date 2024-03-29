# Generated by Django 5.0.1 on 2024-02-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactUs",
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
                ("phone_number", models.CharField(max_length=20)),
                ("is_agreed", models.BooleanField()),
            ],
            options={
                "verbose_name": "contact_us",
                "verbose_name_plural": "contact_us",
            },
        ),
        migrations.CreateModel(
            name="FAQ",
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
                ("title", models.CharField(max_length=255)),
                ("response", models.TextField()),
            ],
            options={
                "verbose_name": "FAQ",
                "verbose_name_plural": "FAQ",
            },
        ),
        migrations.CreateModel(
            name="Image",
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
                ("image", models.ImageField(upload_to="gallery_images/")),
                ("to_show", models.BooleanField()),
            ],
            options={
                "verbose_name": "image",
                "verbose_name_plural": "images",
            },
        ),
        migrations.CreateModel(
            name="Reviews",
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
                ("full_name", models.CharField(max_length=255)),
                ("subtitle", models.CharField(max_length=255)),
                ("review_text", models.TextField()),
            ],
            options={
                "verbose_name": "review",
                "verbose_name_plural": "reviews",
            },
        ),
    ]
