# Generated by Django 3.1.2 on 2020-10-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('offer_id', models.IntegerField(max_length=30, unique=True)),
                ('user', models.EmailField(max_length=30, unique=True)),
            ],
        ),
    ]
