# Generated by Django 5.1.6 on 2025-02-23 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('authoer', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
    ]
