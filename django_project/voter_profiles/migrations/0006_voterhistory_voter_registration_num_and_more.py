# Generated by Django 4.2.11 on 2024-04-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_profiles', '0005_voterhistoryfile_rename_voterfile_regvoterfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='voterhistory',
            name='voter_registration_num',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registeredvotersactive',
            name='registration_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='registeredvotershistorical',
            name='registration_date',
            field=models.DateField(),
        ),
    ]