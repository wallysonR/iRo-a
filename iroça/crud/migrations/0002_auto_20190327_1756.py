# Generated by Django 2.1.4 on 2019-03-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(max_length=500),
        ),
    ]
