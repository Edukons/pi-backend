# Generated by Django 5.1 on 2024-10-11 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0029_delete_familia"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="casa",
            name="data_entrada",
        ),
    ]