# Generated by Django 3.2 on 2022-02-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20220212_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(null=True),
        ),
    ]