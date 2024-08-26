# Generated by Django 5.0.6 on 2024-08-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_animal"),
    ]

    operations = [
        migrations.CreateModel(
            name="Casa",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Prontuario",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=30)),
                ("descricao", models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name="animal",
            name="nome",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]