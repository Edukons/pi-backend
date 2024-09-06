# Generated by Django 5.1 on 2024-09-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0027_remove_familia_nome"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="familia",
            name="pessoas",
        ),
        migrations.AddField(
            model_name="familia",
            name="pessoas",
            field=models.ManyToManyField(related_name="pessoas", to="core.pessoa"),
        ),
    ]
