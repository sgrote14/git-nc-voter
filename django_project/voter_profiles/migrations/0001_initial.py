# Generated by Django 4.2.11 on 2024-04-18 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('county_id', models.IntegerField(primary_key=True, serialize=False)),
                ('county_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CountyCommissioner',
            fields=[
                ('county_commiss_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('county_commiss_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EthnicityCode',
            fields=[
                ('ethnicity_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('ethnicity_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FireDistrict',
            fields=[
                ('fire_dist_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('fire_dist_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GenderCode',
            fields=[
                ('gender_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('gender_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MunicipalDistrict',
            fields=[
                ('munic_dist_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('munic_dist_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('municipality_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('municipality_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PartyCode',
            fields=[
                ('party_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('party_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Precinct',
            fields=[
                ('precinct_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('precinct_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProsecutorialDistrict',
            fields=[
                ('dist_1_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('dist_1_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RaceCode',
            fields=[
                ('race_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('race_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RescueDistrict',
            fields=[
                ('rescue_dist_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('rescue_dist_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SanitationDistrict',
            fields=[
                ('sanit_dist_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('sanit_dist_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolDistrict',
            fields=[
                ('school_dist_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('school_dist_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SewerDistrict',
            fields=[
                ('sewer_dist_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('sewer_dist_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatusCode',
            fields=[
                ('status_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('status_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatusReason',
            fields=[
                ('status_reason_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('status_reason_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Township',
            fields=[
                ('township_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('township_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VoterFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='VoterHistory',
            fields=[
                ('nc_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('county_id', models.IntegerField()),
                ('election_date', models.DateField()),
                ('election_description', models.CharField(max_length=100)),
                ('voting_method', models.CharField(max_length=50)),
                ('voted_party', models.CharField(max_length=5)),
                ('precinct_abbreviation', models.CharField(max_length=6)),
                ('voted_county_id', models.CharField(max_length=6)),
                ('voted_district_label', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='VoterTabulationDistrict',
            fields=[
                ('vtd_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('vtd_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('ward_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('ward_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WaterDistrict',
            fields=[
                ('water_dist_abbrv', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('water_dist_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredVoters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nc_id', models.CharField(max_length=20)),
                ('voter_registration_number', models.CharField(max_length=100)),
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
    ]
