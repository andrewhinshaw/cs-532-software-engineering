# Generated by Django 3.1.3 on 2020-11-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icetrack', '0003_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]
