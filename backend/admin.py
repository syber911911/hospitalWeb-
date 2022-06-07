from django.contrib import admin
from .models import normalH

class normalHAdmin(admin.ModelAdmin):
    list_display = ['id', '기관명', '병원분류명', '응급실운영여부', '주소', '기관ID']
    search_fields = ['기관명']

admin.site.register(normalH, normalHAdmin)
