# Generated by Django 3.0.5 on 2021-10-23 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211023_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendador',
            name='user',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='andar',
            name='user',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='user',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='sala',
            name='user',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]