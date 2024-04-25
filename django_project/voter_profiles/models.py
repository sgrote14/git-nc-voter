from django.db import models


# Create your models here.
class RegVoterFile(models.Model):
    file_date = models.DateTimeField(auto_now_add=False)

    # s3_bucket = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id}: {str(self.file_date)}"


class VoterHistoryFile(models.Model):
    file_date = models.DateTimeField(auto_now_add=False)

    # s3 bucket = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {str(self.file_date)}"


class County(models.Model):
    county_id = models.IntegerField(primary_key=True)
    county_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.county_id}: {self.county_name}"


class StatusCode(models.Model):
    status_code = models.CharField(max_length=2, primary_key=True)
    status_desc = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.status_code}: {self.status_desc}"


class StatusReason(models.Model):
    status_reason_code = models.CharField(max_length=5, primary_key=True)
    status_reason_desc = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.status_reason_code}: {self.status_reason_desc}"


class RaceCode(models.Model):
    race_code = models.CharField(max_length=2, primary_key=True)
    race_desc = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.race_code}: {self.race_desc}"


class EthnicityCode(models.Model):
    ethnicity_code = models.CharField(max_length=5, primary_key=True)
    ethnicity_desc = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ethnicity_code}: {self.ethnicity_desc}"


class PartyCode(models.Model):
    party_code = models.CharField(max_length=5, primary_key=True)
    party_desc = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.party_code}: {self.party_desc}"


class GenderCode(models.Model):
    gender_code = models.CharField(max_length=5, primary_key=True)
    gender_desc = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.gender_code}: {self.gender_desc}"


class Precinct(models.Model):
    precinct_abbrv = models.CharField(max_length=6, primary_key=True)
    precinct_desc = models.CharField(max_length=100)


class Municipality(models.Model):
    municipality_abbrv = models.CharField(max_length=6, primary_key=True)
    municipality_desc = models.CharField(max_length=100)


class Ward(models.Model):
    ward_abbrv = models.CharField(max_length=6, primary_key=True)
    ward_desc = models.CharField(max_length=100)


class CountyCommissioner(models.Model):
    county_commiss_abbrv = models.CharField(max_length=6, primary_key=True)
    county_commiss_desc = models.CharField(max_length=100)


class Township(models.Model):
    township_abbrv = models.CharField(max_length=6, primary_key=True)
    township_desc = models.CharField(max_length=100)


class SchoolDistrict(models.Model):
    school_dist_abbrv = models.CharField(max_length=6, primary_key=True)
    school_dist_desc = models.CharField(max_length=100)


class FireDistrict(models.Model):
    fire_dist_abbrv = models.CharField(max_length=6, primary_key=True)
    fire_dist_desc = models.CharField(max_length=100)


class WaterDistrict(models.Model):
    water_dist_abbrv = models.CharField(max_length=6, primary_key=True)
    water_dist_desc = models.CharField(max_length=100)


class SewerDistrict(models.Model):
    sewer_dist_abbrv = models.CharField(max_length=6, primary_key=True)
    sewer_dist_desc = models.CharField(max_length=100)


class SanitationDistrict(models.Model):
    sanit_dist_abbrv = models.CharField(max_length=6, primary_key=True)
    sanit_dist_desc = models.CharField(max_length=100)


class RescueDistrict(models.Model):
    rescue_dist_abbrv = models.CharField(max_length=6, primary_key=True)
    rescue_dist_desc = models.CharField(max_length=100)


class MunicipalDistrict(models.Model):
    munic_dist_abbrv = models.CharField(max_length=6, primary_key=True)
    munic_dist_desc = models.CharField(max_length=100)


class ProsecutorialDistrict(models.Model):
    dist_1_abbrv = models.CharField(max_length=6, primary_key=True)
    dist_1_desc = models.CharField(max_length=100)


class VoterTabulationDistrict(models.Model):
    vtd_abbrv = models.CharField(max_length=6, primary_key=True)
    vtd_desc = models.CharField(max_length=100)


class RegisteredVotersActive(models.Model):
    nc_id = models.CharField(max_length=100, primary_key=True)
    voter_registration_number = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(default=None, null=True)
    file_id = models.ForeignKey(RegVoterFile, on_delete=models.PROTECT)
    county_id = models.ForeignKey(County, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    name_suffix = models.CharField(max_length=5)
    status_code = models.ForeignKey(StatusCode, on_delete=models.PROTECT)
    status_reason_code = models.ForeignKey(StatusReason, on_delete=models.PROTECT)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=9)
    state = models.CharField(max_length=2)
    mail_address_1 = models.CharField(max_length=100)
    mail_address_2 = models.CharField(max_length=100)
    mail_address_3 = models.CharField(max_length=100)
    mail_address_4 = models.CharField(max_length=100)
    mail_city = models.CharField(max_length=100)
    mail_state = models.CharField(max_length=2)
    mail_zip_code = models.CharField(max_length=9)
    phone_number = models.CharField(max_length=12)
    registration_date = models.DateField(auto_now_add=False)
    race_code = models.ForeignKey(RaceCode, on_delete=models.PROTECT)
    ethnicity_code = models.ForeignKey(EthnicityCode, on_delete=models.PROTECT)
    party_code = models.ForeignKey(PartyCode, on_delete=models.PROTECT)
    gender_code = models.ForeignKey(GenderCode, on_delete=models.PROTECT)
    birth_year = models.IntegerField()
    birth_state = models.CharField(max_length=2)
    drivers_license = models.CharField(max_length=2)
    precinct_abbreviation = models.ForeignKey(Precinct, on_delete=models.PROTECT)
    municipality_abbreviation = models.ForeignKey(Municipality, on_delete=models.PROTECT)
    ward_abbreviation = models.ForeignKey(Ward, on_delete=models.PROTECT)
    congress_dist_abbreviation = models.CharField(max_length=6)
    superior_court_abbreviation = models.CharField(max_length=6)
    judicial_dist_abbreviation = models.CharField(max_length=6)
    nc_senate_abbreviation = models.CharField(max_length=6)
    nc_house_abbreviation = models.CharField(max_length=6)
    county_comm_abbreviation = models.ForeignKey(CountyCommissioner, on_delete=models.PROTECT)
    township_abbreviation = models.ForeignKey(Township, on_delete=models.PROTECT)
    school_dist_abbreviation = models.ForeignKey(SchoolDistrict, on_delete=models.PROTECT)
    fire_dist_abbreviation = models.ForeignKey(FireDistrict, on_delete=models.PROTECT)
    water_dist_abbreviation = models.ForeignKey(WaterDistrict, on_delete=models.PROTECT)
    sewer_dist_abbreviation = models.ForeignKey(SewerDistrict, on_delete=models.PROTECT)
    sanitation_dist_abbreviation = models.ForeignKey(SanitationDistrict, on_delete=models.PROTECT)
    rescue_dist_abbreviation = models.ForeignKey(RescueDistrict, on_delete=models.PROTECT)
    municipal_dist_abbreviation = models.ForeignKey(MunicipalDistrict, on_delete=models.PROTECT)
    prosecutorial_dist_abbreviation = models.ForeignKey(ProsecutorialDistrict, on_delete=models.PROTECT)
    voter_tab_dist_abbreviation = models.ForeignKey(VoterTabulationDistrict, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} + ' ' + {self.last_name}"


class RegisteredVotersHistorical(models.Model):
    nc_id = models.ForeignKey(RegisteredVotersActive, on_delete=models.PROTECT)
    voter_registration_number = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(default=None, null=True)
    file_id = models.ForeignKey(RegVoterFile, on_delete=models.PROTECT)
    county_id = models.ForeignKey(County, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    name_suffix = models.CharField(max_length=5)
    status_code = models.ForeignKey(StatusCode, on_delete=models.PROTECT)
    status_reason_code = models.ForeignKey(StatusReason, on_delete=models.PROTECT)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=9)
    state = models.CharField(max_length=2)
    mail_address_1 = models.CharField(max_length=100)
    mail_address_2 = models.CharField(max_length=100)
    mail_address_3 = models.CharField(max_length=100)
    mail_address_4 = models.CharField(max_length=100)
    mail_city = models.CharField(max_length=100)
    mail_state = models.CharField(max_length=2)
    mail_zip_code = models.CharField(max_length=9)
    phone_number = models.CharField(max_length=12)
    registration_date = models.DateField(auto_now_add=False)
    race_code = models.ForeignKey(RaceCode, on_delete=models.PROTECT)
    ethnicity_code = models.ForeignKey(EthnicityCode, on_delete=models.PROTECT)
    party_code = models.ForeignKey(PartyCode, on_delete=models.PROTECT)
    gender_code = models.ForeignKey(GenderCode, on_delete=models.PROTECT)
    birth_year = models.IntegerField()
    birth_state = models.CharField(max_length=2)
    drivers_license = models.CharField(max_length=2)
    precinct_abbreviation = models.ForeignKey(Precinct, on_delete=models.PROTECT)
    municipality_abbreviation = models.ForeignKey(Municipality, on_delete=models.PROTECT)
    ward_abbreviation = models.ForeignKey(Ward, on_delete=models.PROTECT)
    congress_dist_abbreviation = models.CharField(max_length=6)
    superior_court_abbreviation = models.CharField(max_length=6)
    judicial_dist_abbreviation = models.CharField(max_length=6)
    nc_senate_abbreviation = models.CharField(max_length=6)
    nc_house_abbreviation = models.CharField(max_length=6)
    county_comm_abbreviation = models.ForeignKey(CountyCommissioner, on_delete=models.PROTECT)
    township_abbreviation = models.ForeignKey(Township, on_delete=models.PROTECT)
    school_dist_abbreviation = models.ForeignKey(SchoolDistrict, on_delete=models.PROTECT)
    fire_dist_abbreviation = models.ForeignKey(FireDistrict, on_delete=models.PROTECT)
    water_dist_abbreviation = models.ForeignKey(WaterDistrict, on_delete=models.PROTECT)
    sewer_dist_abbreviation = models.ForeignKey(SewerDistrict, on_delete=models.PROTECT)
    sanitation_dist_abbreviation = models.ForeignKey(SanitationDistrict, on_delete=models.PROTECT)
    rescue_dist_abbreviation = models.ForeignKey(RescueDistrict, on_delete=models.PROTECT)
    municipal_dist_abbreviation = models.ForeignKey(MunicipalDistrict, on_delete=models.PROTECT)
    prosecutorial_dist_abbreviation = models.ForeignKey(ProsecutorialDistrict, on_delete=models.PROTECT)
    voter_tab_dist_abbreviation = models.ForeignKey(VoterTabulationDistrict, on_delete=models.PROTECT)


class VoterHistory(models.Model):
    reg_voter = models.ForeignKey(RegisteredVotersActive, on_delete=models.PROTECT)
    voter_registration_num = models.CharField(max_length=100)
    county_id = models.ForeignKey(County, on_delete=models.PROTECT)
    election_date = models.DateField()
    election_description = models.CharField(max_length=100)
    voting_method = models.CharField(max_length=50)
    voted_party = models.CharField(max_length=5)
    precinct_abbreviation = models.CharField(max_length=6)
    voted_county_id = models.CharField(max_length=6)
    voted_district_label = models.CharField(max_length=6)


class VoterPartyChange(models.Model):
    county_id = models.ForeignKey(County, on_delete=models.PROTECT)
    voter_registration_num = models.CharField(max_length=100)

    active_voter_key = models.ForeignKey(RegisteredVotersActive, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('county_id', 'voter_registration_num')
