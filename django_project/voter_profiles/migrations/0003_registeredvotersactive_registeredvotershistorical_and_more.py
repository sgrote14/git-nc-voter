# Generated by Django 4.2.11 on 2024-04-22 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voter_profiles', '0002_remove_registeredvoters_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredVotersActive',
            fields=[
                ('nc_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('voter_registration_number', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default=None, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('name_suffix', models.CharField(max_length=5)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=9)),
                ('state', models.CharField(max_length=2)),
                ('mail_address_1', models.CharField(max_length=100)),
                ('mail_address_2', models.CharField(max_length=100)),
                ('mail_address_3', models.CharField(max_length=100)),
                ('mail_address_4', models.CharField(max_length=100)),
                ('mail_city', models.CharField(max_length=100)),
                ('mail_state', models.CharField(max_length=2)),
                ('mail_zip_code', models.CharField(max_length=9)),
                ('phone_number', models.CharField(max_length=12)),
                ('registration_date', models.DateTimeField()),
                ('birth_year', models.IntegerField()),
                ('birth_state', models.CharField(max_length=2)),
                ('drivers_license', models.CharField(max_length=2)),
                ('congress_dist_abbreviation', models.CharField(max_length=6)),
                ('superior_court_abbreviation', models.CharField(max_length=6)),
                ('judicial_dist_abbreviation', models.CharField(max_length=6)),
                ('nc_senate_abbreviation', models.CharField(max_length=6)),
                ('nc_house_abbreviation', models.CharField(max_length=6)),
                ('county_comm_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.countycommissioner')),
                ('county_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.county')),
                ('ethnicity_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.ethnicitycode')),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.voterfile')),
                ('fire_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.firedistrict')),
                ('gender_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.gendercode')),
                ('municipal_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.municipaldistrict')),
                ('municipality_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.municipality')),
                ('party_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.partycode')),
                ('precinct_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.precinct')),
                ('prosecutorial_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.prosecutorialdistrict')),
                ('race_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.racecode')),
                ('rescue_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.rescuedistrict')),
                ('sanitation_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.sanitationdistrict')),
                ('school_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.schooldistrict')),
                ('sewer_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.sewerdistrict')),
                ('status_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.statuscode')),
                ('status_reason_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.statusreason')),
                ('township_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.township')),
                ('voter_tab_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.votertabulationdistrict')),
                ('ward_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.ward')),
                ('water_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.waterdistrict')),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredVotersHistorical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_registration_number', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default=None, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('name_suffix', models.CharField(max_length=5)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=9)),
                ('state', models.CharField(max_length=2)),
                ('mail_address_1', models.CharField(max_length=100)),
                ('mail_address_2', models.CharField(max_length=100)),
                ('mail_address_3', models.CharField(max_length=100)),
                ('mail_address_4', models.CharField(max_length=100)),
                ('mail_city', models.CharField(max_length=100)),
                ('mail_state', models.CharField(max_length=2)),
                ('mail_zip_code', models.CharField(max_length=9)),
                ('phone_number', models.CharField(max_length=12)),
                ('registration_date', models.DateTimeField()),
                ('birth_year', models.IntegerField()),
                ('birth_state', models.CharField(max_length=2)),
                ('drivers_license', models.CharField(max_length=2)),
                ('congress_dist_abbreviation', models.CharField(max_length=6)),
                ('superior_court_abbreviation', models.CharField(max_length=6)),
                ('judicial_dist_abbreviation', models.CharField(max_length=6)),
                ('nc_senate_abbreviation', models.CharField(max_length=6)),
                ('nc_house_abbreviation', models.CharField(max_length=6)),
                ('county_comm_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.countycommissioner')),
                ('county_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.county')),
                ('ethnicity_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.ethnicitycode')),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.voterfile')),
                ('fire_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.firedistrict')),
                ('gender_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.gendercode')),
                ('municipal_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.municipaldistrict')),
                ('municipality_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.municipality')),
                ('nc_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.registeredvotersactive')),
                ('party_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.partycode')),
                ('precinct_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.precinct')),
                ('prosecutorial_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.prosecutorialdistrict')),
                ('race_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.racecode')),
                ('rescue_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.rescuedistrict')),
                ('sanitation_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.sanitationdistrict')),
                ('school_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.schooldistrict')),
                ('sewer_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.sewerdistrict')),
                ('status_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.statuscode')),
                ('status_reason_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.statusreason')),
                ('township_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.township')),
                ('voter_tab_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.votertabulationdistrict')),
                ('ward_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.ward')),
                ('water_dist_abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voter_profiles.waterdistrict')),
            ],
        ),
        migrations.AlterField(
            model_name='voterhistory',
            name='nc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    to='voter_profiles.registeredvotersactive'),
        ),
        migrations.AddField(
            model_name='voterhistory',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='RegisteredVoters',
        ),
    ]
