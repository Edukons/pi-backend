# Generated by Django 5.1 on 2024-08-29 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_alter_animal_options"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="fotoAnimal",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
