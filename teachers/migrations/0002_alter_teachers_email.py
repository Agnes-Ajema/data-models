# Generated by Django 5.0.6 on 2024-06-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='email',
            field=models.EmailField(max_length=20),
        ),
    ]
