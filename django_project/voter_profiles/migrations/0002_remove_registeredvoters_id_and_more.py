# Generated by Django 4.2.11 on 2024-04-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeredvoters',
            name='id',
        ),
        migrations.AlterField(
            model_name='registeredvoters',
            name='nc_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='voterhistory',
            name='nc_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
