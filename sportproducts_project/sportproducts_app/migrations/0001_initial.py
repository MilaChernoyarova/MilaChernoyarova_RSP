# Generated by Django 4.2.1 on 2023-06-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('discription', models.CharField(max_length=1000)),
                ('image_url', models.CharField(max_length=1000)),
                ('model', models.CharField(max_length=500)),
            ],
        ),
    ]
