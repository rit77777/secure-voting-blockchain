# Generated by Django 3.2.10 on 2022-03-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220327_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='constituency',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
