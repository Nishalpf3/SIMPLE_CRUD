# Generated by Django 4.2.7 on 2024-05-24 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cls',
            field=models.IntegerField(verbose_name='student class'),
        ),
    ]
