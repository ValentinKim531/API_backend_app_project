# Generated by Django 4.2.8 on 2024-01-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("information", "0002_bookingevent_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="main_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="room/",
                verbose_name="Основное изображение",
            ),
        ),
    ]
