# Generated by Django 3.1.2 on 2020-10-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201026_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='organlist',
            name='donor_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
