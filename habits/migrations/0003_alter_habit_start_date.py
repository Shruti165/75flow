# Generated by Django 5.2.4 on 2025-07-13 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_habit_description_category_habit_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='start_date',
            field=models.DateField(default=datetime.date(2025, 7, 15)),
        ),
    ]
