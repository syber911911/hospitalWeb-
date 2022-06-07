from rest_framework import serializers
from .models import normalH


class normalHSerializer(serializers.ModelSerializer):
    class Meta:
        model = normalH
        fields = ( "주소", "병원분류명", "응급의료기관코드명", "응급실운영여부", "입원가능여부", "기관명", "대표전화1", "응급실전화", "월요진료", "화요진료", "수요진료", "목요진료", "금요진료", "토요진료", "일요진료", "공휴일진료", "기관ID", "병원경도", "병원위도")

class emerHSerializer(serializers.ModelSerializer):
    class Meta:
        model = normalH
        fields = ('기관명', '병원위도','병원경도')