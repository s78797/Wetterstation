# Generated by Django 3.0.2 on 2020-04-20 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='value',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='wind',
            name='direction',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='wind',
            name='speed',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]