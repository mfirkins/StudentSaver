# Generated by Django 3.1.4 on 2020-12-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expendeture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('typeOfExpendeture', models.TextField()),
                ('cost', models.TextField()),
            ],
        ),
    ]
