# Generated by Django 4.0.2 on 2022-03-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_user_alter_issue_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='label',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('D', 'Done'), ('O', 'Ongoing')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='type',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
