# Generated by Django 3.2.9 on 2021-12-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0005_alter_person_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
