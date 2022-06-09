# Generated by Django 4.0.5 on 2022-06-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=60)),
                ('course_number', models.IntegerField(blank=True, default='')),
                ('instructor_name', models.CharField(blank=True, default='', max_length=60)),
                ('duration', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]
