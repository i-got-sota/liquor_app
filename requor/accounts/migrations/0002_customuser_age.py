# Generated by Django 4.0 on 2022-02-06 09:28

import accounts.validate
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(default=20, validators=[accounts.validate.validate_age], verbose_name='年齢'),
            preserve_default=False,
        ),
    ]
