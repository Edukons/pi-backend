# Generated by Django 5.1 on 2024-09-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0025_alter_familia_pessoas"),
    ]

    operations = [
        migrations.AddField(
            model_name="familia",
            name="nome",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
