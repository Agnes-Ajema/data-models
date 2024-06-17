# Generated by Django 5.0.6 on 2024-06-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=10)),
                ('nationality', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('national_id', models.PositiveSmallIntegerField()),
                ('years_of_experience', models.PositiveSmallIntegerField()),
                ('teaching_hours', models.PositiveSmallIntegerField()),
            ],
        ),
    ]