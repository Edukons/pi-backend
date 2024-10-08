# Generated by Django 5.1 on 2024-09-05 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_pessoa_fotopessoa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prontuario",
            name="nome",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="animal",
                to="core.animal",
            ),
        ),
    ]
