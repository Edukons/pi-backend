# Generated by Django 5.1 on 2024-09-06 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_prontuario_animal_alter_prontuario_nome"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prontuario",
            name="nome",
        ),
    ]