# Generated by Django 3.1.3 on 2020-12-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201202_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
