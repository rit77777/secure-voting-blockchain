# Generated by Django 3.2.10 on 2022-03-27 05:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_candidate_party_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='constituency',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('party_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('candidate', models.CharField(max_length=100, null=True)),
                ('party_name', models.CharField(max_length=100, null=True)),
                ('party_pic', models.CharField(blank=True, max_length=500)),
                ('constituency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.constituency')),
            ],
        ),
    ]