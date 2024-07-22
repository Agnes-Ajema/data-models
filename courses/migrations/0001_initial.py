# Generated by Django 5.0.6 on 2024-06-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('trainer', models.CharField(max_length=20)),
                ('duration', models.IntegerField()),
                ('number_of_assessments', models.IntegerField()),
                ('syllabus', models.CharField(max_length=20)),
                ('number_of_assignment', models.IntegerField()),
                ('course_id', models.IntegerField()),
                ('description', models.TextField(max_length=200)),
                ('requirements', models.CharField(max_length=20)),
                ('teaching_materials', models.CharField(max_length=20)),
            ],
        ),
    ]
