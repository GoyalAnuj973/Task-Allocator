# Generated by Django 4.0.2 on 2022-03-03 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assigned_to',
            field=models.CharField(max_length=32),
        ),
    ]