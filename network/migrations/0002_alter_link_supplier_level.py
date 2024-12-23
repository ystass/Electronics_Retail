# Generated by Django 5.1.3 on 2024-12-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="supplier_level",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "завод"),
                    (1, "розничная сеть"),
                    (2, "индивидуальный предприниматель"),
                ],
                null=True,
                verbose_name="Уровень поставщика",
            ),
        ),
    ]
