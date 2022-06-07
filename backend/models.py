from django.db import models

class normalH(models.Model):
    id = models.IntegerField(null=False)
    주소 = models.TextField(blank=True, null=True)
    병원분류명 = models.TextField(blank=True, null=True)
    응급의료기관코드명 = models.TextField(blank=True, null=True)
    응급실운영여부 = models.TextField(blank=True, null=True)
    입원가능여부 = models.TextField(blank=True, null=True)
    기관명 = models.TextField(blank=True, primary_key=True)
    대표전화1 = models.TextField(blank=True, null=True)
    응급실전화 = models.TextField(blank=True, null=True)
    월요진료 = models.TextField(blank=True, null=True)
    화요진료 = models.TextField(blank=True, null=True)
    수요진료 = models.TextField(blank=True, null=True)
    목요진료 = models.TextField(blank=True, null=True)
    금요진료 = models.TextField(blank=True, null=True)
    토요진료 = models.TextField(blank=True, null=True)
    일요진료 = models.TextField(blank=True, null=True)
    공휴일진료 = models.TextField(blank=True, null=True)
    기관ID = models.TextField(blank=True, null=True)  # Field name made lowercase.
    병원경도 = models.TextField(blank=True, null=True)
    병원위도 = models.TextField(blank=True, null=True)



    class Meta:
        managed = False
        db_table = 'normalH'

