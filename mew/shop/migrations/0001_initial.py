# Generated by Django 3.1.3 on 2020-11-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('Desc', models.CharField(max_length=500)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
