# Generated by Django 3.2.5 on 2021-07-04 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizenid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('vehicle', models.CharField(max_length=255)),
                ('bf_date', models.CharField(max_length=255)),
                ('bf_time', models.CharField(max_length=255)),
                ('bf_parish', models.CharField(max_length=255)),
                ('bf_district', models.CharField(max_length=255)),
                ('bf_province', models.CharField(max_length=255)),
                ('bf_country', models.CharField(max_length=255)),
                ('at_parish', models.CharField(max_length=255)),
                ('at_district', models.CharField(max_length=255)),
                ('at_province', models.CharField(max_length=255)),
            ],
        ),
    ]